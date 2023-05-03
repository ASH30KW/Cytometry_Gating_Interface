import axios from "axios";

const APIBaseURL = "/helloworld/";

export class APIService {
  constructor(token) {
    this.instance = axios.create({
      baseURL: APIBaseURL,
      timeout: 1000,
      headers: { Authorization: token },
    });
  }

  getTodos() {
    return this.instance.get("todos/").then((response) => response.data);
  }

  newTodo(task, shared_with) {
    return this.instance
      .post("todos/", { task: task, shared: shared_with })
      .then((response) => response.data);
  }

  deleteTodo(id) {
    return this.instance.delete(`todos/${id}`);
  }
}
