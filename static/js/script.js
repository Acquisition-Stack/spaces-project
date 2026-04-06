//YouTube Video Player API
var tag = document.createElement("script");
tag.src = "https://www.youtube.com/iframe_api";
document.head.appendChild(tag);

var player;
var isMuted = false;

//Hide YouTube Player
function onYouTubeIframeAPIReady() {
  player = new YT.Player("player", {
    height: "0",
    width: "0",
    videoId: "OO2kPK5-qno",
    playerVars: {
      autoplay: 1,
    },
  });
}

//Mute Youtube Player
document.querySelector(".mute-button").addEventListener("click", () => {
  if (isMuted) {
    player.unMute();
    isMuted = false;
  } else {
    player.mute();
    isMuted = true;
  }
});
