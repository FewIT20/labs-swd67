function deleteProject(pro_id, csrf_token){
    const action = {
        "action": "deleteProject"
    }
    // กำหนด path ให้ถูกต้อง
    fetch(`/project/${pro_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(action)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item deleted successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}