import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../usuario/usuario';


const API_URL = "http://localhost:5000/"


@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  loggedIn : boolean = false;

  idLogged: string = "";

  constructor( private http: HttpClient) { 
    console.log("Usuario API lista")
  }

  httpOptions = {
    headers: new HttpHeaders({ "Content-Type": "application/json" })
  };

  get_usuario(id:string){
    return this.http.get(API_URL + 'get_usuario/' + id);
  }

  createUsuario(usuario: Usuario){
    return this.http.post(API_URL + 'create_usuario', usuario, this.httpOptions);
  }

  addPreferencias(preferencias: any[]){
    return this.http.post(API_URL + 'add_preferencias', preferencias, this.httpOptions);
  }

  get_recomendaciones_by_id(id:string){
    return this.http.get(API_URL + 'get_recomendaciones/' + id, this.httpOptions);
  }

  getLogStatus (){
    return this.loggedIn;
  }

  setLogStatus (status: boolean){
    
    this.loggedIn = status;
  }

  get_artistas_populares(){
    return this.http.get(API_URL + 'get_popular_artists');
  }

  get_artistas(){
    return this.http.get(API_URL + 'get_artists');
  }

}
