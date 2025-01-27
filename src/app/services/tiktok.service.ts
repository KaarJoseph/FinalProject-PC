import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root', // Servicio disponible globalmente
})
export class TiktokService {
  private baseUrl: string = 'http://127.0.0.1:5000'; // URL del servidor Flask

  constructor(private http: HttpClient) {}

  ejecutarExtraccion(): Observable<any> {
    return this.http.post('http://127.0.0.1:5000/ejecutar_extraccion', {});
  }
  
  // Método para obtener los comentarios
  getComentarios(): Observable<any> {
    return this.http.get(`${this.baseUrl}/obtener_comentarios`);
  }
}
