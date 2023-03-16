const { Component, xml, mount, useState } = owl;

class PlayList extends Component {
    static template = xml`
    <div id="PlayList" style="float:right">
        <h2>PlayList</h2>
    </div>`
}
class Player extends Component {
    static template = xml`
  <div>
    <h2 id="song-title">Song Title</h2>
    <div id="player-controls">
        <button id="pause-button" t-on-click="pauseThisSong">Pause</button>
        <button id="play_btn" t-on-click="playThisSong">Play</button>
        <button id="stop-button" t-on-click="stopThisSong">Stop</button>
    </div>
  </div>`;
    playThisSong() {
      if (!audio) {
        return;
      }
      audio.play();
    }
    pauseThisSong() {
      if (!audio) {
        return;
      }
      audio.pause();
    }
    stopThisSong() {
      if (!audio) {
        return;
      }
      audio.pause();
      audio.currentTime = 0;
    }
  }

let audio = '';
class MusicList extends Component {
    static template = xml`
    <div id="MusicList" style="float:left">
        <t t-if="props.searchData[0] and props.searchData[0] !== 'Song not Found'">
            <h2>List of Songs</h2>
            <t t-foreach="props.searchData[0]" t-as="song" t-key="song-id">
                <p><t t-out ="song.name"/></p>
                <button t-att-value="song.url" t-on-click="addSongToPlayList">Add to playlist</button>
                <button t-att-value="song.url" t-on-click="playSong">Play song</button>
            </t>
            </t>
    </div>
    <Player/>`;

    playSong(ev){
        if (audio) {
            audio.pause();
            audio.currentTime = 0;
          }
          const selectedSongUrl = ev.target.getAttribute('value');
          const selectedSong = this.props.searchData[0].find(song => song.url === selectedSongUrl);
          document.getElementById('song-title').textContent = selectedSong.name;
          audio = new Audio(selectedSongUrl);
          audio.play();
        }
    addSongToPlayList(ev){
        const selectedSongUrl = ev.target.getAttribute('value');
        const selectedSong = this.props.searchData[0].find(song => song.url === selectedSongUrl);
        }
        setup(){
            this.storeData = useState([])
        }
    static components = {Player}
    }
    
    
class Search extends Component {
    static template = xml `
    <div style="border:1px,solid,black;text-align:center">
        <input type="text" id="searchSong" placeholder="Search a music" value="Freedom"/>
        <button t-on-click="getMusic" id="SearchButton">Search</button>
        <MusicList searchData="searchData"/>
    </div>`;

    setup(){
        this.searchData = useState([]); 
     }
     async getMusic() {
         const findSong = document.getElementById('searchSong').value;
         const response = await fetch(`/music/search?song_name=${findSong}`);
         const {result: newData} = await response.json();
         this.searchData.push(newData);
         console.log(this.searchData[0])
 
     }
    static components = {MusicList};
}

class Root extends Component {
    static template = xml `
    <Search/>
    <PlayList/>`;
    

    static components = {Search,PlayList}
}

window.onload = function(){
    mount(Root, document.body);
};

