import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'; // Importar HttpClientModule
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent, // Componente principal
  ],
  imports: [
    BrowserModule,
    HttpClientModule, // Importar módulo HTTP para usar el servicio
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
