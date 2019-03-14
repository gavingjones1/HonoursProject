function scrollingText(){
    var para1 = 'At first glance, this webpage looks a lot like facebook. It is extremely easy for hackers to recreate the facebook web page and you would not know the difference. Try typing in any email and password (not your own! Does not have to be real) into the sign in boxes on the top right of the web page. Once done, close the browser window.';
    var para2 = 'It is extremely easy for hackers to recreate the facebook web page and you would not know the difference.';
    var para3 = 'Try typing in any email and password (not your own! Does not have to be real) into the sign in boxes on the top right of the web page. Once done, close the browser window.';
    var i=0
    var paragraphs = [para1, para2, para3];

    

    // function paragraphscroller(){
    //     for(var parano=0; parano<paragraphs.length; parano++){
    //         setInterval(parano);
    //     }
    // }
    setInterval(function() { 
        if (i < para1.length ){
             document.getElementById('popup').innerHTML += para1[i];
                i++;
        
        
        
                // if (i < para2.length ){
        //     document.getElementById('popup').innerHTML += para2[i];
        //         i++;  
        // if (i < para3.length ){
        //     document.getElementById('popup').innerHTML += para3[i];
        //         i++;
            // if (j < paragraphs[i].length){
            //     document.getElementById('popup').innerHTML += paragraphs[i][j];
            //     j++;
            // } else {
                
            //     i++;
                
            // }
        }
    //paragraphscroller()
    }, 50);
}
