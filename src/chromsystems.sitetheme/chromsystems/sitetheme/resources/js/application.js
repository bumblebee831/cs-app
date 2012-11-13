/*jslint white:false, onevar:true, undef:true, nomen:true, eqeqeq:true, plusplus:true, bitwise:true, regexp:true, newcap:true, immed:true, strict:false, browser:true */
/*global jQuery:false, document:false, window:false, location:false */

(function ($) {
    $(document).ready(function () {
        if (jQuery.browser.msie && parseInt(jQuery.browser.version, 10) < 7) {
            // it's not realistic to think we can deal with all the bugs
            // of IE 6 and lower. Fortunately, all this is just progressive
            // enhancement.
            return;
        }
        $('form[data-appui="ajaxsubmit"]').on('submit', function (e) {
            e.preventDefault();
            var name = $('#item-title').val();
            var htmlString = '<div class="tile tile-header sortable"><h5>' + name + '</h5></div>';
            $(htmlString).hide().prependTo("#dropbox").fadeIn("slow");
            $(this)[0].reset();
        });
        $('div.sortable')
            .drag("start", function (ev, dd) {
                $(this).addClass('dragging');
                return $(this).clone()
                    .css("opacity", '.75')
                    .appendTo(this.parentNode);
            })
            .drag(function (ev, dd) {
                $(dd.proxy).css({
                    top: dd.offsetY,
                    left: dd.offsetX
                });
                var drop = dd.drop[0],
                method = $.data(drop || {}, "drop+reorder");
                if (drop && (drop != dd.current || method != dd.method)) {
                    $(this)[method](drop);
                    dd.current = drop;
                    dd.method = method;
                    dd.update();
                }
            })
            .drag("end", function (ev, dd) {
                $(this).removeClass('dragging');
                $(dd.proxy).remove();
                $('#btn-cancel').fadeOut('slow', function () {
                    $('#btn-save').fadeIn('slow');
                });
            })
            .drop("init", function (ev, dd) {
                return !(this == dd.drag);
            });
        $.drop({
            tolerance: function (event, proxy, target) {
                var test = event.pageY > (target.top + target.height / 2);
                $.data(target.elem, "drop+reorder", test ? "insertAfter" : "insertBefore");
                return this.contains(target, [ event.pageX, event.pageY ]);
            }
        });
    });
}(jQuery));
