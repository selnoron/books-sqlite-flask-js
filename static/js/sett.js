let title = $("#title"),
    author= $("#author")

class Booking{
    constructor(){
        this.APIBook = "/api/v1/books";
    }

    setboo = async () => {
        return await Request.post(this.APIBook, {
            "title" : title[0].value,
            "author" : author[0].value
        })
    }
}

$("#set").click(async (e)=>{
    e.preventDefault();
    let settu = new Booking();
    let result = await settu.setboo();
    result = JSON.parse(result);
    console.log(result);
    if (result == 0){
        location.href="";
    }else{
        console.log("Ошибка данных");
    }
})