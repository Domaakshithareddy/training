let ticketNumber = 1001;

const employeeName = document.getElementById("employeeName");
const category = document.getElementById("category");
const priority = document.getElementById("priority");
const description = document.getElementById("description");
const message = document.getElementById("message");
const container = document.getElementById("ticketContainer");
const totalTickets = document.getElementById("totalTickets");
const openTickets = document.getElementById("openTickets");
const resolvedTickets = document.getElementById("resolvedTickets");

let total = 0;
let open = 0;
let resolved = 0;

document.getElementById("submitBtn").addEventListener("click", createTicket);

function createTicket(){

    message.innerHTML="";

    if(employeeName.value.trim()==""){
        message.innerHTML="Employee name is required";
        return;
    }

    if(category.value==""){
        message.innerHTML="Select issue category";
        return;
    }

    if(priority.value==""){
        message.innerHTML="Select priority";
        return;
    }

    if(description.value.trim()==""){
        message.innerHTML="Issue description is required";
        return;
    }

    const ticket=document.createElement("div");

    ticket.classList.add("ticket");

    let priorityClass=priority.value.toLowerCase();

    ticket.classList.add(priorityClass);

    const ticketID="TKT-"+ticketNumber++;

    ticket.innerHTML=`
    <h3>${ticketID}</h3>
    <p><strong>Employee :</strong> ${employeeName.value}</p>
    <p><strong>Category :</strong> ${category.value}</p>
    <p><strong>Priority :</strong> ${priority.value}</p>
    <p><strong>Description :</strong> ${description.value}</p>
    <p class="status"><strong>Status :</strong> Open</p>
    <button class="resolve">Resolve</button>
    <button class="delete">Delete</button>
    `;

    container.prepend(ticket);

    total++;
    open++;

    updateCounter();

    employeeName.value="";
    category.value="";
    priority.value="";
    description.value="";

    const resolveBtn=ticket.querySelector(".resolve");
    const deleteBtn=ticket.querySelector(".delete");
    const status=ticket.querySelector(".status");

    resolveBtn.addEventListener("click",function(){
        status.innerHTML="<strong>Status :</strong> Resolved";
        resolveBtn.disabled=true;
        open--;
        resolved++;
        updateCounter();
    });

    deleteBtn.addEventListener("click",function(){

        if(confirm("Delete this ticket?")){
            if(status.innerText.includes("Resolved")){
                resolved--;
            }else{
                open--;
            }

            total--;
            ticket.remove();
            updateCounter();
        }
    });
}

function updateCounter(){
    totalTickets.innerHTML=total;
    openTickets.innerHTML=open;
    resolvedTickets.innerHTML=resolved;
}