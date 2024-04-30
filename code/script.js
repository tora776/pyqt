function displayUsers() {
    fetch('/get_users')
    .then(response => response.json())
    .then(data => {
        const userList = document.getElementById('userList');
        userList.innerHTML = '';

        data.forEach(user => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${user.name}</td>
                <td>${user.address}</td>
                <td>${user.tel}</td>
                <td>${user.mail}</td>
                <td><button onclick="deleteUser(${user.id})">削除</button></td>
            `;
            userList.appendChild(row);
        });
    });
}

function addUser() {
    const name = document.getElementById('name').value.trim();
    const address = document.getElementById('address').value.trim();
    const tel = document.getElementById('tel').value.trim();
    const mail = document.getElementById('mail').value.trim();

    if (!name || !address || !tel || !mail) {
        alert('すべてのフィールドを入力してください。');
        return;
    }

    fetch('/add_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            address: address,
            tel: tel,
            mail: mail
        })
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('name').value = '';
            document.getElementById('address').value = '';
            document.getElementById('tel').value = '';
            document.getElementById('mail').value = '';
            displayUsers();
        } else {
            alert('データの追加中にエラーが発生しました。');
        }
    });
}

function deleteUser(userId) {
    fetch('/delete_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: userId
        })
    })
    .then(response => {
        if (response.ok) {
            displayUsers();
        } else {
            alert('データの削除中にエラーが発生しました。');
        }
    });
}