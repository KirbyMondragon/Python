const getSleepHours = (day) =>{
    var days = ["Monday", "Tuesday" , "Wednesday" ,"Thursday","Friday","Saturday", "Sunday"];
    var vuelta = 0;
    var hours = 8;
    while(day != days[vuelta])
    {
      vuelta++;
      hours*vuelta;
  
      if(day == days[vuelta])
      {
        console.log("You need to sleep " + hours );
      }
    }
  }
  var day = "monday"; 
  console.log(getSleepHours(day));