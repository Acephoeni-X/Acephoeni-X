let sizes:any = function(obj:any) {
    var size = 0, key: string;
    for (key in obj) {
      if (obj.hasOwnProperty(key)) size++;
    }
    return size;
  };
class student{
    async getData() {
        let res = await fetch('https://api.github.com/users/Rishi-Sharma2002/repos')
        let data = res.json();
        return data;
    }

    async getLanguages() {
        let promise_data = await this.getData();
        let json_language:object;
        console.log(promise_data)
        json_language = {
            "Python":0,
            "C++":0,
            "JavaScript":0,
            "C":0 
        };
        for (let i:number=0; i<sizes(promise_data); i++){
            for (var k in json_language){
                if (k == promise_data[i].language){
                    json_language[k] ++;
                }
            }
        }
        return json_language;
    }
}

let s = new student;
