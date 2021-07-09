let sizes = function(obj) {
    var size = 0, key;
    for (key in obj) {
      if (obj.hasOwnProperty(key)) size++;
    }
    return size;
  };

async function getData(){
    let res = await fetch('https://api.github.com/users/Rishi-Sharma2002/repos')
    let data = res.json();
    return data;
}

async function getLanguages(){
    let promise_data = await getData();
    let json_language;
    console.log(promise_data)
    json_language = {
        "Python":0,
        "C++":0,
        "JavaScript":0,
        "C":0 
    };

return json_language;