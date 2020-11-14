const apiEndpoint = '/api/';

const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        greeting: 'Hello, Vue!',
        flaskGreeting: '',
        todoList:[],
    },
    created: async function(){
        const gResponse = await fetch(apiEndpoint + 'todos/');
        const gObject = await gResponse.json();
        this.todoList = gObject;
    }
})