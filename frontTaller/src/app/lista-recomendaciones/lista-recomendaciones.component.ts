import { Component, OnInit } from '@angular/core';
import { UsuarioService } from '../services/usuario.service';

@Component({
  selector: 'app-lista-recomendaciones',
  templateUrl: './lista-recomendaciones.component.html',
  styleUrls: ['./lista-recomendaciones.component.css']
})
export class ListaRecomendacionesComponent implements OnInit {

  recomendaciones : any[] = [];

  usersImportantes : any[] = [];

  imageToShow: any;
  isImageLoading: any;

  createImageFromBlob(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
        this.imageToShow = reader.result;
    }, false);

    if (image) {
        reader.readAsDataURL(image);
    }
  }



  constructor(private usuarioService: UsuarioService) { 
    this.usuarioService.get_recomendaciones_by_id(usuarioService.idLogged).subscribe((data:any)=>{
      console.log(data);

      //Carga Imagen
      this.isImageLoading = true;
      this.usuarioService.get_grafo().subscribe((dataImg:any)=>{
        console.log(dataImg);
        this.createImageFromBlob(dataImg);
        this.isImageLoading = false;

      }, error =>{
        this.isImageLoading = false;
        console.log(error);
      });

      
      // console.log(JSON.parse(data["recommendaciones"]));
      console.log(JSON.parse(data["usuarios"]));
      // console.log(data["features"]);

      this.recomendaciones = data["recommendaciones"];
      this.usersImportantes = JSON.parse(data["usuarios"]);
      // this.features = data["features"];

      

    });
  }

  ngOnInit(): void {
  }

}
