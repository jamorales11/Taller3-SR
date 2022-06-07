import { Component, OnInit } from '@angular/core';
import { UsuarioService } from '../services/usuario.service';
import { Usuario } from './usuario';

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrls: ['./usuario.component.css']
})
export class UsuarioComponent implements OnInit {

  usuario: Usuario = new Usuario();

  constructor(private usuarioService: UsuarioService) { 
    this.usuarioService.get_usuario(usuarioService.idLogged).subscribe((data:any) => {
      console.log(data);

     console.log(data[0]);

     console.log(usuarioService.idLogged);

      this.usuario.userId = usuarioService.idLogged;

      console.log(this.usuario);

    })
  }

  ngOnInit(): void {
  }

}
