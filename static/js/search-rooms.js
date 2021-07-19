/* ====================== [ Slide Bar JS ] ====================== */

$(".slidebar-wrap").stick_in_parent({
    offset_top: 120
});

/* ====================== [ End Slide Bar JS ] ====================== */

/* ====================== [ Button Add Reservation JS ] ====================== */

$(".button-add").click( function(){
    var value = $(this).closest(".rooms-detail-fit").find(".select-room-add").val();
    $(this).closest(".rooms-detail-fit").find(".remove-wrap").css("display","block");
    $(this).closest(".rooms-detail-fit").find(".add-number").text(value);
    var room_name = $(this).closest(".rooms-detail-fit").find(".name-rooms").text();
    if (room_name.indexOf(' ') >= 0) {
        var room_name= room_name.substr(0, room_name.indexOf(' '));
    }
    $(this).closest(".infor-rooms-search").find(".amount_" + room_name).val(value);
})

$(".remove-button").click( function(){
    var value = $(this).closest(".rooms-detail-fit").find(".select-room-add").val();
    $(this).closest(".rooms-detail-fit").find(".remove-wrap").css("display","none");
    var room_name = $(this).closest(".rooms-detail-fit").find(".name-rooms").text();
    if (room_name.indexOf(' ') >= 0) {
        var room_name= room_name.substr(0, room_name.indexOf(' '));
    }
    $(this).closest(".infor-rooms-search").find(".amount_" + room_name).val('0');
})

/* ====================== [ End Button Add Reservation JS ] ====================== */