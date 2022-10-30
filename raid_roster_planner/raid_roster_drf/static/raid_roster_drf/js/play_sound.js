function play_sound() {
  const audio = new Audio('/static/raid_roster_drf/audio/fart-with-reverb.mp3')
  audio.play();
}

$(document).ready(function(){
  $('#footer_orc_head').click(play_sound);
});
