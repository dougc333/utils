const {exec} = require("child_process")

exec("ls -al",(error,stdout,err)=>{
    console.log(`stdout:${stdout}`)
    let a:string = `${stdout}`
});

