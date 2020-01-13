jQuery.wait= function (ms) {
     var defer = $.Deferred();
     setTimeout(function () {
         defer.resolve();
     }, ms);
     return defer;
};

