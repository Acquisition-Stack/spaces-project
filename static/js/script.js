//YouTube Video Player API
var tag = document.createElement("script");
tag.src = "https://www.youtube.com/iframe_api";
document.head.appendChild(tag);

//Hide YouTube Player
function onYouTubeIframeAPIready() {
  player = new YT.Player("player", {
    height: "0",
    width: "0",
    playerVars: {
      listType: "playlist",
      list: "RDuxRRuHH4po8",
      autoplay: 1,
    },
    events: {
      onStateChange: onPlayerStateChange,
    },
  });
}
