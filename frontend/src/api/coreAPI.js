import axios from "axios";

const APIBaseURL = "/core/";

export class APIService {
  constructor(token) {
    this.instance = axios.create({
      baseURL: APIBaseURL,
      timeout: 10000,
      headers: { Authorization: token },
    });
  }

  // PROXY

  getWithProxy(options) {
    const { url } = options;
    return this.instance.post("/proxy/", { method: "GET", url });
  }

  // ARCHITECTURE

  getEnabledPlugins() {
    return this.instance
      .get("/architecture/plugins/enabled")
      .then((response) => response.data);
  }

  // USER

  login(username, pw) {
    return this.instance
      .post("/user/login", { name: username, password: pw })
      .then((response) => response.data);
  }

  logout() {
    return this.instance.get("/user/logout").then((response) => response.data);
  }

  self() {
    return this.instance.get("/user/self").then((response) => response.data);
  }

  changePassword(oldPassword, newPassword) {
    return this.instance
      .post("/user/changepw", {
        password: oldPassword,
        newPassword: newPassword,
      })
      .then((response) => response.data);
  }

  getUsers() {
    return this.instance.get("/user/").then((response) => response.data);
  }

  addUser(username, password, role) {
    return this.instance
      .post("/user/", {
        name: username,
        password: password,
        role: role,
      })
      .then((response) => response.data);
  }

  updateUser(uuid, username, password, role) {
    return this.instance
      .post("/user/updateuser", {
        uuid: uuid,
        name: username,
        password: password,
        role: role,
      })
      .then((response) => response.data);
  }

  deleteUser(uuid) {
    return this.instance
      .delete("/user/", { data: { uuid: uuid } })
      .then((response) => response.data);
  }

  getGroups() {
    return this.instance.get("/groups/").then((response) => response.data);
  }

  getGroupsByUser() {
    return this.self().then((me) => {
      return this.getGroups().then((grps) => {
        return grps.filter((x) => me.groups.includes(x.uuid));
      });
    });
  }

  addGroup(groupname) {
    return this.instance
      .post("/groups/", { name: groupname })
      .then((response) => response.data);
  }

  deleteGroup(uuid) {
    return this.instance
      .delete(`/groups/${uuid}`)
      .then((response) => response.data);
  }

  renameGroup(uuid, name) {
    return this.instance
      .post(`/groups/${uuid}`, { name: name })
      .then((response) => response.data);
  }

  groupAddSomething(group_uuid, something_uuid, what) {
    return this.instance
      .post(`/groups/${group_uuid}/${what}s`, { uuid: something_uuid })
      .then((response) => response.data);
  }

  groupRemoveSomething(group_uuid, something_uuid, what) {
    return this.instance
      .delete(`/groups/${group_uuid}/${what}s`, {
        data: { uuid: something_uuid },
      })
      .then((response) => response.data);
  }

  groupAddUser(group_uuid, user_uuid) {
    return this.groupAddSomething(group_uuid, user_uuid, "user");
  }

  groupRemoveUser(group_uuid, user_uuid) {
    return this.groupRemoveSomething(group_uuid, user_uuid, "user");
  }

  groupAddOwner(group_uuid, user_uuid) {
    return this.groupAddSomething(group_uuid, user_uuid, "owner");
  }

  groupRemoveOwner(group_uuid, user_uuid) {
    return this.groupRemoveSomething(group_uuid, user_uuid, "owner");
  }

  groupAddSubgroup(group_uuid, subgroup_uuid) {
    return this.groupAddSomething(group_uuid, subgroup_uuid, "subgroup");
  }

  groupRemoveSubgroup(group_uuid, subgroup_uuid) {
    return this.groupRemoveSomething(group_uuid, subgroup_uuid, "subgroup");
  }
}
