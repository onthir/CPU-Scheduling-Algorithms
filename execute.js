console.log("Executing First Come First Serve Algorithm")

// create rectangele
// create svg element:


// function to create process i.e. rectangel
function create_processes(){
    console.log("Creating Processes");
    var svg = d3.select("#rect").append("svg").attr("width", 50).attr("height", 200)

    // Add the path using this helper function
    svg.append('rect')
      .attr('x', 10)
      .attr('y', 120)
      .attr('width', 50)
      .attr('height', 40)
      .attr('stroke', 'black')
      .attr('fill', '#69a3b2')
      .attr('label', "P1");
    svg.append("g");
}



function logSubmit(event) {
    console.log("form submitted");
    log.textContent = `Form Submitted! Time stamp: ${event.timeStamp}`;
    event.preventDefault();
  }
  

const form = document.getElementById('processForm');
const log = document.getElementById('log');

if (form){
    form.addEventListener("submit", logSubmit, false)
}

