define(['module/bootstrap'], function(news) {
    'use strict';

    var trackShareToolsVisible = function() {
        var shareToolsVisible = false;

        news.$(window).on('scroll', function() {
            var shareTools = news.$('#share-tools');
            if(elementInView(shareTools) && !shareToolsVisible) {
                shareToolsVisible = true;
                news.pubsub.emit('shareTools:visible');
            }
        });
    };

    function elementInView(elem) {

        if(!$(elem) || !$(elem).offset()) {
          return false;
        }

        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height();

        var elemTop = $(elem).offset().top;
        var elemBottom = elemTop + $(elem).height();

        return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop)) === true;
    }

    var trackFirstUserScroll = function() {
        news.$(window).one('scroll', function() {
            news.pubsub.emit('user:firstscroll');
        });
    };

    var init = function() {
        trackFirstUserScroll();
        trackShareToolsVisible();
    };

    return {
        init: init
    };
});
