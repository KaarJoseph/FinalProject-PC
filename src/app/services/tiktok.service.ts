import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root', // Asegura que el servicio esté disponible globalmente
})
export class TiktokService {
  private baseUrl: string = 'http://127.0.0.1:5000'; // URL del servidor Flask

  constructor(private http: HttpClient) {}

  getComentarios(): Observable<any> {
    return this.http.get(`${this.baseUrl}/obtener_comentarios`);
  }
}
