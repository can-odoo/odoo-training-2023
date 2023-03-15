const { Component, mount, xml ,useState} = owl

class MusicList extends Component {
    static template = xml`
        <div>
            
        </div>
    `;
    static props = [ 'searchData' ];
}
class Search extends Component {
    static template = xml`
        <div style="border:1px; text-align:center">
            <input type="text" id="searchSong" placeholder="Search here" value="Freedom"/>
            <button t-on-click="getMusic" is="searchButton">Search</button>
            <MusicList searchData='searchData'/>
        </div>
    `;

    setup(){
        this.searchData = useState([]);
    }    
    async getMusic() {
        const findSong = document.getElementById('searchSong').value;
        const response = await fetch(`/music/search?song_name=${findSong}`);
        const {result : newData} = await response.json();
        this.searchData.push(newData);
    }

    static components = { MusicList }
}

class Root extends Component {
    static template = xml`
        <div>
            <Search/>
        </div>
        
    `;

    static components = { Search };
}

window.onload = function () {
    mount(Root, document.body);
}