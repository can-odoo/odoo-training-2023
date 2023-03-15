/** @odoo-module **/

const { Component ,xml,mount,useState}  = owl;

class MusicList extends Component{
    static template = xml`
    <div>
        Hello
    </div>
    `
    // static props = ['searchData']
}

class Search extends Component{
    static template = xml`
    <div style="border:1px,solid,black;text-align:center">
            <input type="text" id="searchSong" placeholder="Search a music" value="Freedom"/>
            <button t-on-click="getMusic" id="searchButton" >Search</button>
            <MusicList />
    </div>
    `;

    setup(){
        this.searchData = useState([]);
    }

    async getMusic(){
        const findSong = document.getElementById('searchSong').value;
        const response = await fetch(`/music/search?song_name=${findSong}`)
        console.log(response);
        const {result:newData} = await response.json();
        this.searchData.push(newData);  
    }

    static components = {MusicList}
}

class Root extends Component{
    static template = xml`
    <div>
    I am root
    </div>
    <Search/>
    `
    static components= {Search}
}

window.onload=function(){
    mount(Root,document.body);
}