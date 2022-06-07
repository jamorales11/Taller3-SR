import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UsuarioService } from '../services/usuario.service';

@Component({
  selector: 'app-preferencias',
  templateUrl: './preferencias.component.html',
  styleUrls: ['./preferencias.component.css']
})
export class PreferenciasComponent implements OnInit {

  movies : any[] = [];
  seleccionadas: any[] = [];
  
  seleccion: string= "";
  calificacion: number = 0;

  seleccionCompleta: boolean = false;

  constructor(private usuarioService: UsuarioService, private router: Router) {

    this.usuarioService.get_movies().subscribe((data:any)=>{
      this.movies = JSON.parse(data["movies"]);
      console.log(this.movies);
    });
   }


  ngOnInit(): void {
  }


  agregarDeBuscador(){

    if(this.seleccion != ""){
      let peli = this.movies.find(element => element['title'] == this.seleccion);
      console.log(this.calificacion);


      peli.rating = Number(this.calificacion);

      console.log(peli);
    
      if(!this.seleccionadas.includes(peli)){
        this.seleccionadas.push(peli);
        
        console.log(this.seleccionadas);

        

      }
    }

        this.seleccion = "";
        this.calificacion = 0;
    
    if(this.seleccionadas.length == 10){
      this.seleccionCompleta = true;
    }
  }


 isOnList(value:string){
  if(this.seleccionadas.includes(value)){
    return true;
  }
  return false;
 }

 onGuardar(){
   console.log(this.seleccionadas);
   let incidencias : any[] = []; 
   let i = 0;
   while(i<this.seleccionadas.length){

    let j = 10-i;

    while(j>0){
      let incidencia = {"user_id": this.usuarioService.idLogged,'movie_id': this.seleccionadas[i].movie_id, "rating": this.seleccionadas[i].rating, 'timestamp': ""};
      incidencias.push(incidencia);
      j--;
    }
    i++;
   }
   console.log(incidencias);
   this.usuarioService.addPreferencias(incidencias).subscribe(() => {
    this.router.navigate(["/usuario"]);

   });
 }

 

eliminar(index:number){
  this.seleccionadas.splice(index,1);
  if(this.seleccionadas.length < 10){
    this.seleccionCompleta = false;
  } 
}

}
