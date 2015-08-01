/**
 * Created by forest on 15.
 */

(function($) {

    $('#hero, #why_us, #utp, #about, .panel-register').appear();

    $(document.body).on('appear', '#hero, #why_us, #utp, #about, .panel-register', function(e, $affected) {
        $(this).addClass('active');
        if($(this).hasClass('inverse')){
            //$('#primary').addClass('inverse');
            if($('#primary').find('.active.inverse').length != 0){
                $('#primary').addClass('inverse');
            }
        }
    });

    $(document.body).on('disappear', '#hero, #why_us, #utp, #about, .panel-register', function(e, $affected) {
        $(this).removeClass('active');

        if($('#primary').find('.active.inverse').length == 0){
            $('#primary').removeClass('inverse');
        }

    });


    $('#utp_entries').slick({
        slide:      'li',
        autoplay:   true,
        arrows:     false,
        dots:       true
    });
/*

    $('.response-entries').slick({
        //slide:      'article',
        mobileFirst: true,
        respondTo: 'min',
        autoplay:   true,
        arrows:     false,
        dots:       true
    }); */

    if($('#photoupload').length > 0){
    $('#photoupload').dropzone({
        url: '/model/up',
        dictDefaultMessage: 'Перенесите фото для загрузки или кликните для выбора'
    });
    }

    /*= Repeatable inputs ======================================= */

    var price_item_index=0;
    $('#add_price_item').click(function(){

        price_item_index++;
        $(this).before($('#price_item_form').clone().attr('id','price_item_form' + price_item_index));
        $('#price_item_form' + price_item_index).removeClass('hidden');
        $('#price_item_form' + price_item_index + ' :input, #price_item_form' + price_item_index + ' :button').each(function() {
            $(this).attr('name', $(this).attr('name') + price_item_index);
            $(this).attr('id', $(this).attr('id') + price_item_index);
        });
        $('#remove_price_item' + price_item_index).click(function(){
            $(this).closest('div').remove();
        });
    });

    var link_item_index=0;
    $('#add_link_item').click(function(){

        link_item_index++;
        $(this).before($('#link_item_form').clone().attr('id','link_item_form' + link_item_index));
        $('#link_item_form' + link_item_index).removeClass('hidden');
        $('#link_item_form' + link_item_index + ' :input, #link_item_form' + link_item_index + ' :button').each(function() {
            $(this).attr('name', $(this).attr('name') + link_item_index);
            $(this).attr('id', $(this).attr('id') + link_item_index);
        });
        $('#remove_link_item' + link_item_index).click(function(){
            $(this).closest('div').remove();
        });
    });
    /*= END Repeatable inputs ======================================= */


    //$('.nav').on('show.bs.dropdown', function () {
    //    console.log(' do something…');
    //});
    //$('.nav').on('shown.bs.dropdown', function () {
    //    console.log(' do something…');
    //});

    $('.dropdown-select').on('click', 'a', function(e){
        $(this).closest('ul').find('li.active').removeClass('active');
        $(this).closest('li').addClass('active');
        //$(this).closest('div').find('input').val($(this).text());
        $(this).closest('.dropdown').find('.label-text').text($(this).text());
        e.preventDefault();
    });


if($('#calendar').length > 0){
    var ratio = $(window).width() <= 767 ? .5 : 1;
    $('#calendar').fullCalendar({
        header: {
            left: 'title',
            center: '',
            right: 'prev,next today month,agendaWeek,agendaDay'
        },
        eventRender: function (event, element, view) {
            var nextEventLeft = element.offset().left + element.width() + 5;
            element.parent().children().eq(element.index()+1).css('left',nextEventLeft);
        },
        defaultDate: '2015-05-12',
        editable: true,
        eventLimitClick: 'day',
        aspectRatio:ratio,
        views: {
            month: {
                //eventLimit: ($(window).width() <= 767)? 2 : 6 // adjust to 6 only for agendaWeek/agendaDay
            }
        },
        windowResize: function(view) {
            if($(window).width() <= 767){
                $('#calendar').fullCalendar( 'changeView', 'month' );
                $('#calendar').fullCalendar('option', 'aspectRatio', .5);
            }else{
                $('#calendar').fullCalendar('option', 'aspectRatio', 1);
            }
        },
        eventLimit: true, // allow "more" link when too many events
        events: [
            {
                title: 'All Day Event',
                start: '2015-05-01',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Long Event',
                start: '2015-05-07',
                end: '2015-05-10',
                className: 'fc-event-width-overirde'
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: '2015-05-09T16:00:00',
                className: 'fc-event-width-overirde'
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: '2015-05-16T16:00:00',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Conference',
                start: '2015-05-11',
                end: '2015-05-13',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Meeting',
                start: '2015-05-12T10:30:00',
                end: '2015-05-12T12:30:00',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Lunch',
                start: '2015-05-12T12:00:00',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Meeting',
                start: '2015-05-12T14:30:00',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Happy Hour',
                start: '2015-05-12T17:30:00',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Dinner',
                start: '2015-05-12T20:00:00',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Birthday Party',
                start: '2015-05-13T07:00:00',
                className: 'fc-event-width-overirde'
            },
            {
                title: 'Click for Google',
                url: 'http://google.com/',
                start: '2015-05-28',
                className: 'fc-event-width-overirde'
            }
        ]
    });
}


}(jQuery));