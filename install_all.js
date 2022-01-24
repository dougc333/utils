const {exec} = require("child_process")
const {fs}=require('fs')

exec("ls -al",(error,stdout,err)=>{
    console.log(`stdout:${stdout}`)
    console.log(typeof(`${stdout}`)) 
    let lines = `${stdout}`.split('\n')
    console.log(lines.length)
    lines.forEach(x=>{
        y=x.split(" ")
        console.log("y length:",y.length)
        file_or_dir = y[y.length-1]
        console.log("file_or_dir:",file_or_dir)
        if (file_or_dir!==null){
            let isDir=fs.existsSync(file_or_dir)
            console.log(file_or_dir,isDir)
        }
        
    })
});

