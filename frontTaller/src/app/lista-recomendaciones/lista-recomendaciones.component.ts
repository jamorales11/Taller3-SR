import { Component, OnInit } from '@angular/core';
import { UsuarioService } from '../services/usuario.service';

@Component({
  selector: 'app-lista-recomendaciones',
  templateUrl: './lista-recomendaciones.component.html',
  styleUrls: ['./lista-recomendaciones.component.css']
})
export class ListaRecomendacionesComponent implements OnInit {

  recomendaciones : any[] = [];

  features : any[] = [];

  usersImportantes : any[] = [];



  constructor(private usuarioService: UsuarioService) { 
    this.usuarioService.get_recomendaciones_by_id(usuarioService.idLogged).subscribe((data:any)=>{
      console.log(data);
      // console.log(JSON.parse(data["recommendaciones"]));
      // console.log(JSON.parse(data["usuarios"]));
      // console.log(data["features"]);

      // this.recomendaciones = JSON.parse(data["recommendaciones"]);
      // this.usersImportantes = JSON.parse(data["usuarios"]);
      // this.features = data["features"];

      

    });
  }

  ngOnInit(): void {
  }

}
