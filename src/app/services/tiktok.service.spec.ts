import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TiktokService {
  private baseUrl = 'http://127.0.0.1:5000'; // URL base del servidor Flask

  constructor(private http: HttpClient) {}

  // Obtener comentarios desde el servidor Flask
  getComentarios(): Observable<any> {
    return this.http.get(`${this.baseUrl}/obtener_comentarios`);
  }

  // Subir un archivo CSV al servidor Flask
  subirArchivo(archivo: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', archivo);

    return this.http.post(`${this.baseUrl}/subir_csv`, formData);
  }
}
