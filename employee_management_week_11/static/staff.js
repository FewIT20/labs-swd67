function addStaff(id, csrf_token){
    const emp = document.getElementById('input-add-staff');
    const data = {
        emp_id: emp.value
    };

    // กำหนด path ให้ถูกต้อง
    fetch(`/project/${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}

async function removeStaff(id, emp_Id, csrf_token){

    // กำหนด path ให้ถูกต้อง
    const action = {
        "action": "removeStaff",
        "emp_id": emp_Id
    }
    fetch(`/project/${id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(action)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}