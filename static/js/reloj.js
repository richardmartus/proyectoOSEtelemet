showDateTime(); // Llama a la función para mostrar la fecha y hora actual

function showDateTime() {
  const daysOfWeek = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];
  const months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];

  myDate = new Date();
  dayOfWeek = daysOfWeek[myDate.getDay()];
  day = myDate.getDate();
  monthName = months[myDate.getMonth()];
  year = myDate.getFullYear();
  hours = myDate.getHours();
  minutes = myDate.getMinutes();
  seconds = myDate.getSeconds();

  // Formatea los valores para asegurarte de que tengan dos dígitos
  if (day < 10) day = "0" + day;
  if (hours < 10) hours = "0" + hours;
  if (minutes < 10) minutes = "0" + minutes;
  if (seconds < 10) seconds = "0" + seconds;

  $("#HoraActual").text(`${dayOfWeek} ${day} de ${monthName} de ${year}  ${hours}:${minutes}:${seconds}`);


  setTimeout(showDateTime, 1000);
}


