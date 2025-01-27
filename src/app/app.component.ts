import { Component, OnInit } from '@angular/core';
import { TiktokService } from './services/tiktok.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'frontend';
  tiktokData: any[] = [];
  mensaje: string = '';

  constructor(private tiktokService: TiktokService) {}

  ngOnInit(): void {
    this.obtenerComentarios();
  }

  extraerInformacion(): void {
    this.tiktokService.ejecutarExtraccion().subscribe({
      next: (response) => {
        console.log('Extracción realizada:', response);
        this.obtenerComentarios(); // Cargar los comentarios extraídos
      },
      error: (err) => {
        console.error('Error al extraer información:', err);
        this.mensaje = 'Ocurrió un error al realizar la extracción.';
      }
    });
  }
  

  obtenerComentarios(): void {
    this.tiktokService.getComentarios().subscribe({
      next: (data) => {
        this.tiktokData = data;
        console.log('Comentarios obtenidos:', this.tiktokData);
      },
      error: (err) => {
        console.error('Error al obtener los comentarios:', err);
        this.mensaje = 'No se pudieron cargar los datos de TikTok.';
      }
    });
  }
  
}
