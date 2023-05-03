import axios from "axios";

const APIBaseURL = "/cytometrygating/";

export class APIService {
  constructor() {
    // (token)
    this.instance = axios.create({
      baseURL: APIBaseURL,
      timeout: 5000000,
      //headers: {'Authorization': token}
    });
  }

  // Manual Gating
  getImgs(ImgsType, id) {
    return this.instance
      .get(`cytometrygating/Imgs/${ImgsType}/${id}`)
      .then((respone) => respone.data);
  }
  getFeature() {
    return this.instance
      .get(`cytometrygating/Features`)
      .then((respone) => respone.data);
  }
  postNewData(ids) {
    return this.instance
      .post(`cytometrygating/NewData`, { PointsIndex: ids })
      .then((respone) => respone.data);
  }
  //Machine Learning supported Gating
  getClusterData(Feature, xlabel, ylabel) {
    return this.instance
      .get(`cytometrygating/Cluster/${Feature}/${xlabel}/${ylabel}`)
      .then((respone) => respone.data);
  }
  getClusterImg(id) {
    return this.instance
      .get(`cytometrygating/ClusterImg/${id}`)
      .then((respone) => respone.data);
  }
}
