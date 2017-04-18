document.getElementById("nav_bar").innerHTML =
    
    '<head>' +
        '<style type="text/css">' +
    
            '#navbar {' +
                'list-style-type: none;' +
                'margin: 0;' +
                'padding: 0;' +
                'overflow: hidden;' +
                'background-color: #333;' +
            '}' +
    
            '.navbar_item {' +
                'float: left;' +
            '}' +

            '.navbar_item a {' +
                'display: block;' +
                'color: white;' +
                'text-align: center;' +
                'padding: 14px 16px;' +
                'text-decoration: none;' +
            '}' +

            '.navbar_item a:hover {' +
                'background-color: #111;' +
            '}' +
    
        '</style>' +
    '</head>' +
    
    '<body>' +
        '<ul id = "navbar">' +
    
            '<li class="navbar_item"><a class="navbar_link" href="static/templates/index.html" target="_top">Streamer Surf</a></li>' +

            '<li class="navbar_item"><a class="navbar_link" href="../model/streamers.html" target="_top">Streamers</a></li>' +

            '<li class="navbar_item"><a class="navbar_link" href="../model/games.html" target="_top">Games</a></li>' +

            '<li class="navbar_item"><a class="navbar_link" href="../model/genres.html" target="_top">Genres</a></li>' +

            '<li class="navbar_item" style="float: right;"><a class="navbar_link" href={{url_for('about')} target="_top">About</a><li>' +
        
        '</ul>' +
    '</body>';