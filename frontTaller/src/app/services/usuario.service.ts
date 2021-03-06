import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../usuario/usuario';


const API_URL = "http://172.24.41.184:8081/"


@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  loggedIn : boolean = false;

  idLogged: number = 0;

  constructor( private http: HttpClient) { 
    console.log("Usuario API lista")
  }

  httpOptions = {
    headers: new HttpHeaders({ "Content-Type": "application/json" })
  };

  httpOptions2 = {
    headers: new HttpHeaders({ "Content-Type": "image/png" })
  };

  get_usuario(id:number){
    return this.http.get(API_URL + 'get_usuario/' + id);
  }

  createUsuario(usuario: Usuario){
    return this.http.post(API_URL + 'create_usuario', usuario, this.httpOptions);
  }

  addPreferencias(preferencias: any[]){
    return this.http.post(API_URL + 'add_preferencias', preferencias, this.httpOptions);
  }

  get_recomendaciones_by_id(id:number){
    return this.http.get(API_URL + 'get_recomendaciones/' + id, this.httpOptions);
  }

  get_grafo(){
    return this.http.get(API_URL + 'get_grafo', { responseType: 'blob' });
  }

  getLogStatus (){
    return this.loggedIn;
  }

  setLogStatus (status: boolean){
    
    this.loggedIn = status;
  }


  get_movies(){
    return this.http.get(API_URL + 'get_movies');
  }

}
