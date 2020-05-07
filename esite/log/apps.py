# -*- coding: utf-8 -*-
import os
import io
import logging

from django.conf import settings
from django.apps import AppConfig

from telethon import TelegramClient, events
from telethon.tl.custom import Button
#from .file_handler import progress
#import os
import time
import datetime
import asyncio
import threading
import json
import re
import string

from datetime import datetime

# BOX object


class BOX:
    # meths
    @classmethod
    def os(cls, os):
        return {
            'posix': lambda: '/opt/ts3soundboard/',
            'nt': lambda: 'C:\\SinusBot\\',
            'mac': lambda: os.sys.exit()
        }.get(os, lambda: cls.help)()

    @classmethod
    def commands(cls, cmd):
        # input: lowercase string splitted by ":"
        # output: [0] - the text message,[1] - buttons
        cmd = cmd.split(":")[0]
        print(cmd)
        return {
            'info': lambda: cls.info,
            'start': lambda: cls.start,
            'back': lambda: cls.start,
            'workpackages': lambda: cls.workpackages,
            'todo': lambda: cls.todo,
            'wp': lambda: cls.workpackage,
            'wp_start': lambda: cls.workpackage_start,
            'wp_commit_handler': lambda: cls.workpackage_commit,
            'wp_commit': lambda: cls.commit,
        }.get(cmd, lambda: cls.help)()

    @classmethod
    def info(cls, **kwargs):
        event = kwargs["event"]

        text = f'Your TelegramID: {event.query.user_id}'

        return (text, [
            [Button.inline('Back')],
        ])

    @classmethod
    def start(cls, **kwargs):
        print(kwargs)
        from .models import Workpackage
        workpackages = Workpackage.objects.filter(status="ongoing")
        """ Ongoing packages overview """
        """
        000-000-000 SNEKLOG RUNNING-TIME by schettn
        000-000-001 SNEKLOG RUNNING-TIME by cisco
        """
        print("overivew")
        overview = [
            f'`{workpackage.pid} {workpackage.name} {workpackage.realtime} by {workpackage.assoc_user}`'
            for workpackage in workpackages
        ]
        overview_text = '`Ongoing Workpackages:`\n\n' + '\n'.join(overview)
        print(overview_text)

        if "event" in kwargs:
            event = kwargs["event"]
            from django.contrib.auth import get_user_model

            users = get_user_model().objects.filter(
                telegram_id=event.query.user_id)
            my_workpackages = []
            if (len(users) > 0):
                my_workpackages = Workpackage.objects.filter(
                    assoc_user=users[0], status="ongoing")
            print("user")
            print("USER:", users)
            # case1: a user have n ongoing packages
            #   -> print a overview of all ongoing packages
            #   -> Show workpackages button
            #   -> Show my todo list
            #
            if (len(my_workpackages) > 0):
                return (overview_text, [
                    [
                        Button.inline('Workpackages', data=b'workpackages'),
                        Button.inline('Todo', data=b'todo')
                    ],
                    [Button.inline('Info')],
                ])

        return (overview_text, [
            [Button.inline('Workpackages', data=b'workpackages')],
            [Button.inline('Info')],
        ])

    @classmethod
    def workpackages(cls, **kwargs):
        from .models import Workpackage
        print(kwargs["event"])
        user_id = kwargs["event"].query.user_id
        workpackages = Workpackage.objects.all()
        button_list = [[
            Button.inline(f"{workpackage.pid} {workpackage.name}",
                          data=(f"wp:{workpackage.pid}").encode())
        ] for workpackage in workpackages]
        button_list.append([Button.inline('Back')])

        new_count = Workpackage.objects.filter(status='new').count()
        ongoing_count = Workpackage.objects.filter(status='ongoing').count()
        waiting_count = Workpackage.objects.filter(status='waiting').count()
        review_count = Workpackage.objects.filter(status='review').count()
        fin_count = Workpackage.objects.filter(status='fin').count()

        overview_text = f"`New: {new_count}\nOngoing: {ongoing_count}\nWaiting: {waiting_count}\nWaiting for Review: {review_count}\nFinished: {fin_count}`"

        return (overview_text, button_list)

    @classmethod
    def workpackage(cls, **kwargs):
        print(kwargs)
        event = kwargs["event"]

        from django.contrib.auth import get_user_model
        from .models import Workpackage

        user_id = event.query.user_id
        data = event.query.data.decode("utf-8").lower()
        print(data)
        pid = data.split(":")[1]
        print(pid)
        workpackage = Workpackage.objects.get(pid=pid)
        wp_out = f"`{workpackage.name}\nstatus: {workpackage.status}\ndurration: {workpackage.durration}\nrealtime: {workpackage.realtime}\nsid: {workpackage.sid}\ndid: {workpackage.did}\npid: {workpackage.pid}`"

        users = get_user_model().objects.filter(
            telegram_id=event.query.user_id)
        if (len(users) > 0):
            workpackage_check = Workpackage.objects.filter(pid=pid,
                                                           assoc_user=users[0])
            print(workpackage_check)
            if (len(workpackage_check) > 0):
                if (workpackage.status == 'new'
                        or workpackage.status == 'waiting'):
                    return (wp_out, [[
                        Button.inline(
                            'Start',
                            data=(f"wp_start:{workpackage.pid}").encode()),
                        Button.inline(
                            'Back',
                            data=(f"back:wp:{workpackage.pid}").encode())
                    ]])
                if (workpackage.status == 'review'
                        or workpackage.status == 'fin'):
                    return (wp_out, [[
                        Button.inline(
                            'Back',
                            data=(f"back:wp:{workpackage.pid}").encode())
                    ]])
                return (wp_out,
                        [[
                            Button.inline(
                                'Commit',
                                data=(f"wp_commit:{workpackage.pid}").encode())
                        ],
                         [
                             Button.inline(
                                 'Back',
                                 data=(f"back:wp:{workpackage.pid}").encode())
                         ]])
            print("false")
        return (wp_out, [[
            Button.inline('Back', data=(f"back:wp:{workpackage.pid}").encode())
        ]])

        # state = ('Nothing', 'wp_nothing')
        # if(user):
        #     if(workpackage.status == 'new'):
        #         state = ('Start', 'wp_start')
        #     if(workpackage.status == 'ongoing'):
        #         state = ('Stop', 'wp_stop')

        # if(workpackage.status == 'fin')
        #     pass#no button

        # if(work)

        # return (wp_out, [[Button.inline(state[0], data=(f"{state[1]}:{workpackage.pid}").encode()), Button.inline('Back', data=(f"back:wp:{workpackage.pid}").encode())]])
    @classmethod
    def todo(cls, **kwargs):
        event = kwargs["event"]

        from django.contrib.auth import get_user_model
        from .models import Workpackage

        users = get_user_model().objects.filter(
            telegram_id=event.query.user_id)
        button_list = []
        if (len(users) > 0):
            workpackages = Workpackage.objects.filter(assoc_user=users[0])
            button_list = [[
                Button.inline(
                    f"[{workpackage.status}] {workpackage.pid} {workpackage.name} ",
                    data=(f"wp:{workpackage.pid}").encode())
            ] for workpackage in workpackages]

        button_list.append([Button.inline('Back')])

        return (f'`Your workpackages:`', button_list)

    @classmethod
    def workpackage_start(cls, **kwargs):
        print(kwargs)
        event = kwargs['event']
        from .models import Workpackage

        data = event.query.data.decode("utf-8").lower()
        pid = data.split(":")[1]

        workpackage = Workpackage.objects.get(pid=pid)
        workpackage.status = "ongoing"
        workpackage.starttime = datetime.now()
        workpackage.save()

        wp_out = f"`{workpackage.name}\nstatus: {workpackage.status}\ndurration: {workpackage.durration}\nrealtime: {workpackage.realtime}\nsid: {workpackage.sid}\ndid: {workpackage.did}\npid: {workpackage.pid}`"
        print("before crash")
        return cls.workpackage(event=event)

    @classmethod
    def workpackage_commit(cls, **kwargs):
        print(kwargs)
        event = kwargs['event']
        from .models import Workpackage

        data = event.query.data.decode("utf-8").lower()
        cmd, pid, status = data.split(":")

        workpackage = Workpackage.objects.get(pid=pid)
        workpackage.status = status
        workpackage.save()

        wp_out = f"`{workpackage.name}\nstatus: {workpackage.status}\ndurration: {workpackage.durration}\nrealtime: {workpackage.realtime}\nsid: {workpackage.sid}\ndid: {workpackage.did}\npid: {workpackage.pid}`"
        print("before crash")
        return cls.workpackage(event=event)

    @classmethod
    def commit(cls, **kwargs):
        # Stop
        # Note
        # Request Review
        print("HEYDIHOE")
        event = kwargs['event']
        print(event)
        data = event.query.data.decode("utf-8").lower()
        pid = data.split(":")[1]

        from .models import Workpackage

        workpackage = Workpackage.objects.get(pid=pid)
        return (
            f'`{workpackage.name}`',
            [
                [
                    Button.inline(
                        'Stop',
                        data=(f"wp_commit_handler:{pid}:waiting").encode()),
                    #Button.inline('Note', data=(f"wp_note:{pid}").encode())
                ],
                [
                    Button.inline(
                        'Request Review',
                        data=(f"wp_commit_handler:{pid}:review").encode())
                ],
                [Button.inline('Back')]
            ])

    @classmethod
    def help(cls, **kwargs):
        return ("useable commands and arguments are", [
            [
                Button.inline('Workpackages', data=b'workpackages'),
                Button.inline('Start')
            ],
        ])
        # return ('useable commands and arguments are:\n\thelp\t--help -h\n\tadd\t--add -a\n\texit\t--exit -e', [])


class LogConfig(AppConfig):
    name = 'esite.log'

    def ready(self):
        """Start the client."""
        print("sneklog started...")
        log_thread = threading.Thread(name="log-main-thread", target=Log.main)
        log_thread.daemon = True  # -> dies after main thread is closed
        log_thread.start()


class Log():
    def main():
        loop = asyncio.new_event_loop()
        client = TelegramClient(
            'anon',
            settings.TELEGRAM_API_ID,
            settings.TELEGRAM_API_HASH,
            loop=loop).start(bot_token=settings.TELEGRAM_BOT_TOKEN)

        @client.on(events.CallbackQuery)
        async def callback(event):
            data = event.query.data.decode("utf-8").lower()
            print(data)
            cmd_out = BOX.commands(data)(event=event)
            # print(workpackages)
            # if(workpackages):
            #     print("true1")
            #     cmd_out= BOX.commands(data)(event,workpackages)
            #     print("true")
            # else:
            #     print("false")
            #     cmd_out= BOX.commands(data)(event)
            #     print("false")

            #workpackages = cmd_out[3]
            # print(event.query.user_id)
            # print(event.query.__dict__.keys())
            # print(event.query.data.decode("utf-8"))
            # print(BOX.commands(event.query.data.decode("utf-8").lower())()[0])
            # print(cmd_out)
            await client.edit_message(event.chat_id,
                                      event.query.msg_id,
                                      cmd_out[0],
                                      buttons=cmd_out[1])

        def funcname(parameter_list):
            pass

        @client.on(events.NewMessage(pattern='/start'))
        @client.on(events.NewMessage(pattern='/help'))
        async def start(event):
            """Send a message when the command /start is issued."""
            await event.respond(
                "Hi, I'm an audio slave! :3\nI would love to convert every wav you got into a telegram voice message. (>.<)"
            )
            raise events.StopPropagation

        @client.on(events.NewMessage(pattern='/init'))
        async def start(event):
            """Send a message when the command /start is issued."""
            cmd_out = BOX.commands('start')()
            print(cmd_out)
            await event.respond(cmd_out[0], buttons=cmd_out[1])

            raise events.StopPropagation

        @client.on(events.NewMessage)
        async def echo(event):
            """Echo the user message."""
            # if telegram message has attached a wav file, download and convert it
            if event.message.file and event.message.file.mime_type == 'audio/x-wav':
                msg = await event.respond("Processing...")

                try:
                    #start = time.time()

                    await msg.edit("**Downloading start...**")

                    # audio_in = io.BytesIO()
                    #audio_in.name = f"{event.message.file.name.split('.')[0]}_snek_{event.message.date.strftime('%m-%d_%H-%M')}.wav"
                    # audio_in = await client.download_media(event.message, audio_in, progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    #     progress(d, t, msg, start)))

                    # audio_seg = AudioSegment.from_wav(audio_in)

                    # audio_out = io.BytesIO()
                    # audio_out = audio_seg.export(audio_out, bitrate="128k", format='ogg', codec="opus", parameters=["-strict", "-2", "-ac", "2", "-vol", "150"], tags={"ARTIST": "waveater", "GENRE": "Meeting/Trashtalk", "ALBUM": "waveater", "TITLE": f"{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}", "DATE": f"{event.message.media.document.date.strftime('%Y/%m/%d_%H:%M:%S')}", "COMMENT": f"A wav file converted to telegram voice message.", "CONTACT":"@waveater"})
                    # audio_out.name = f"{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}.ogg"
                    # print(len(audio_seg)//1000)
                    # print(event.message.file.id)
                    # print(event.message.file.title)
                    # print(event.message.file.performer)
                    # print(event.message.file.name)
                    # print(event.message.file.duration)
                    result = await client.send_file(
                        event.chat_id,
                        audio_out,
                        voice_note=True,
                        caption=
                        f"{event.message.message}\n\n`track: '{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}',\nchannel: '{audio_seg.channels}'',\nformat: 'ogg',\ncodec: 'opus',\nbitrate: '128k'`",
                        reply_to=event.message)
                    # print(result.file.duration)
                    # print(result.file.performer)

                    await msg.delete()

                except Exception as e:
                    print(e)
                    await msg.edit(
                        f"OwO Shit happens! Something has gone wrong.\n\n**Error:** {e}"
                    )

        # print(f"{threading.enumerate()}")
        client.run_until_disconnected()


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2020 miraculix-org Florian Kleber
