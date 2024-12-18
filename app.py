import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from datetime import datetime, timedelta
#from CoreMailClient import CoreMail
from send_email import send_email
from google_calendar_classV2 import GoogleCalendarManager

#config
st.set_page_config(page_title="CPK Autos & Maquinaria Pesada", page_icon="🚗⚙️", layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
   with open(file_name) as f:
       st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/styles.css")
email_address ="emailcontact@gmail.com"

lottie_file ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"

with st.container():
    izq_column, middle_column, der_column = st.columns([1, 2, 1])
    with middle_column:
        image = Image.open("images/Logo.png")
        st.image(image, use_container_width=True, width=300)
        #st.image(image, use_container_width=True)
    st.title("Tu taller de confianza para reparación y mantenimiento de vehículos y maquinaria pesada.")
    st.write(
        "Bienvenidos al taller mecánico de confianza para vehículos y maquinaria pesada."
    )
    #st.write("[Saber más >](https://valerapp.com/)")

    st.markdown(
    """
    <style>
    /* Cambiar el color de las pestañas activas e inactivas */
    div[role="tablist"] > div {
        color: red !important; /* Texto de la pestaña */
        background-color:rgb(192, 31, 31); /* Fondo de la pestaña */
        border-radius: 5px; /* Bordes redondeados */
        margin-right: 5px; /* Espaciado entre pestañas */
        padding: 5px 15px; /* Espaciado interno */
        cursor: pointer;
    }

    /* Estilo de la pestaña activa */
    div[role="tablist"] > div[aria-selected="true"] {
        background-color:rgb(175, 75, 75); /* Fondo rojo más oscuro */
        color: white !important; /* Texto blanco */
        border: 2px solid red; /* Borde */
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Crear pestañas
    tabs = st.tabs(
        ["Servicios", "Reseñas", "Portafolio", "Contacto"]
    ) 
   

    # Pestaña Servicios
    with tabs[0]:

        #button = f"""
        #</form>
        #   <input type="hidden" name="_captcha" value="false">
        #    <button type="submit">Reservar</button>
        #</form>"""

        #email = f"""
        #   <form action="https://formsubmit.co/{email_address}" method="POST">
        #</form>"""

        

        # Simulación de horas disponibles
        # Configuramos un horario de trabajo (por ejemplo, 10:00 a 18:00)
        hora_inicio = 10  # 10:00 AM
        hora_fin = 18  # 6:00 PM
        intervalo = 60  # Intervalo de 60 minutos

# Generar opciones de horas disponibles
        horas_disponibles = []
        hora_actual = datetime.strptime(f"{hora_inicio}:00", "%H:%M")
        while hora_actual.hour < hora_fin:
            horas_disponibles.append(hora_actual.strftime("%H:%M"))
            hora_actual += timedelta(minutes=intervalo)


        #servicios = {
         #    "Auto - 50 $": 50,
          #  "Grúa Horquilla - 30 $": 30,
         #   "Camión Minero - 20 $": 20,
        #    "Retroexcavadora - 400 $": 400  }

        vehiculos_servicios = {
    "Auto": {
        "Cambio de aceite": 30,
        "Reparación de frenos": 100,
        "Cambio de neumáticos": 150,
        "Reparación de suspensión": 200
    },
    "Grúa Horquilla": {
        "Reemplazo de batería": 150,
        "Mantenimiento hidráulico": 300,
        "Inspección de motor": 250,
        "Reparación de frenos": 180
    },
    "Camión Minero": {
        "Reparación de motor": 500,
        "Mantenimiento de neumáticos": 400,
        "Inspección de sistema de frenos": 350,
        "Reemplazo de piezas de desgaste": 600
    },
    "Retroexcavadora": {
        "Reparación de motor": 400,
        "Mantenimiento de sistemas hidráulicos": 350,
        "Reparación de tren de rodaje": 500,
        "Inspección de la pala": 200
        }
        }

        

        st.markdown(
        """
            <style>
            div.stButton > button {
                background-color: #90EE90; /* Verde claro */
                color: white; /* Texto blanco */
                border: 2px solid #006400; /* Borde verde oscuro */
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            div.stButton > button:hover {
                background-color: #32CD32; /* Verde más intenso al pasar el cursor */
            }
            </style>
        """,unsafe_allow_html=True
        )




        
        #st.write("[Más sobre nosotros>](https://valerapp.com/about/)")
    

        # servicios
        with st.container():
            st.header("Nuestros servicios")
            st.write("---")
            image_column, text_column = st.columns((1,2))
            with image_column:
                image = Image.open("images/auto.jpg")
                st.image(image, use_container_width=True)
            with text_column:
                st.subheader("Reparación de Autos")
                st.markdown("""Servicio integral para el mantenimiento y reparación de automóviles, enfocado en garantizar su seguridad, rendimiento y durabilidad.
Incluye:

* Diagnóstico computarizado del motor.\n
* Reparación de frenos, embrague y suspensión.\n
* Ajuste de transmisión y caja de cambios.\n
* Servicio eléctrico: batería, alternador y luces.\n
* Cambio de aceite, filtros y revisión de fluidos.\n
* Reparación de sistemas de inyección y escape.""")
            st.write("---")
            image_column, text_column = st.columns((1,2))
            with image_column:
                image = Image.open("images/images.jpeg")
                st.image(image, use_container_width=True)
            with text_column:
                st.subheader("Reparación de Grúas Horquillas")
                st.markdown(
                    """ 
Mantenimiento y reparación especializada en grúas horquillas (montacargas) para garantizar un funcionamiento óptimo en operaciones logísticas e industriales.
Incluye:

* Diagnóstico de sistemas hidráulicos y neumáticos.\n
* Reparación y calibración de sistemas de elevación.\n
* Mantenimiento de motores eléctricos y de combustión.\n
* Sustitución de neumáticos y rodajes.\n
* Diagnóstico de baterías y sistemas eléctricos.\n
* Ajuste de frenos y dirección.
                    """
                )
            #st.write("[Ver servicios >](https://valerapp.com/services/)")

        with st.container():
            st.write("---")
            st.write("##")
            image_column, text_column = st.columns((1,2))
            with image_column:
                image = Image.open("images/camion-minero.jpeg")
                st.image(image, use_container_width=True)
            with text_column:
                st.subheader("Reparación de Camiones Mineros")
                st.markdown(
                    """
                    Servicios de mantenimiento y reparación enfocados en camiones mineros de alto tonelaje, garantizando su resistencia y operación continua en entornos extremos.
Incluye:

* Diagnóstico y reparación de motores diésel de alto rendimiento.\n
* Mantenimiento de sistemas de frenos hidráulicos y neumáticos.\n
* Revisión y ajuste de la transmisión y diferenciales.\n
* Reparación de sistemas eléctricos y electrónicos.\n
* Servicio de suspensión y chasis reforzados.\n
* Monitoreo y ajuste de sistemas de refrigeración.\n
                    """
                )
            #st.write("[Ver servicios >](https://valerapp.com/services/)")

        with st.container():
            st.write("---")
            st.write("##")
            image_column, text_column = st.columns((1,2))
            with image_column:
                image = Image.open("images/Retroexcavadora.jpg")
                st.image(image, use_container_width=True)
            with text_column:
                st.subheader("Reparación de Retroexcavadoras")
                st.markdown(
                    """
                    Servicio especializado para retroexcavadoras, con el fin de garantizar su eficiencia operativa en trabajos de construcción, excavación y movimiento de tierra.
Incluye:

* Diagnóstico completo de motores y sistemas hidráulicos.\n
* Reparación de bombas y cilindros hidráulicos.\n
* Ajuste y mantenimiento de brazos, plumas y baldes.\n
* Servicio de transmisión, caja de cambios y ejes.\n
* Revisión de neumáticos y orugas.\n
* Reparación de sistemas eléctricos y electrónicos.\n
                    """
                )
        st.write("---")
        st.header("Reserva tu cita")
        left_column, right_column = st.columns((1,2))
        with left_column:
            nombre = st.text_input("Tu nombre")
            date = st.date_input("Fecha")
            vehiculo = st.selectbox("Selecciona el tipo de vehículo", list(vehiculos_servicios.keys()))
            if vehiculo:
                servicios = vehiculos_servicios[vehiculo]
                servicio_seleccionado = st.selectbox("Selecciona el servicio", options=list(servicios.keys()))
            #servicio_seleccionado = st.selectbox("Servicios",options=list(servicios.keys()))
            reservar = st.button("Reservar")
        with right_column:
            # Campo de selección: Horas disponibles
            hora_seleccionada = st.selectbox("Horas disponibles", options=horas_disponibles)
            email = st.text_input("Tu email")
            st.text_input("Deja tu mensaje aqui")
        if reservar:
            if not nombre or not email or not servicios:
                st.warning("Tienes que rellenar todos los campos obligatorios antes de reservar tu cita")
            else:
                try:
                    # Crear hora de inicio y fin del evento
                    parsed_time = datetime.strptime(hora_seleccionada, "%H:%M").time()
                    start_time = datetime.combine(date, parsed_time)
                    end_time = start_time + timedelta(minutes=30)

                    # Crear evento en Google Calendar
                    calendar_manager = GoogleCalendarManager()
                    calendar_manager.create_event(
                        summary=f"{vehiculo} - {servicio_seleccionado} - {nombre}",
                        start_time=start_time.isoformat(),
                        end_time=end_time.isoformat(),
                        timezone="America/Santiago",
                        attendees=[email]
                    )
                    send_email(email,nombre,str(date),str(hora_seleccionada),servicio_seleccionado)

                    st.success("¡Reserva realizada con éxito! Revisa tu correo para confirmar.")
                    st.success("Tu cita ha sido reservada. Revisa tu correo para ver el mensaje de confirmacion")
                except Exception as e:
                    st.error(f"Error al procesar la reserva: {str(e)}")
        
        st.write("---")
        # Encabezado de la sección
        st.write("### ¡Síguenos en nuestras redes sociales!")

        # Contenedor para centrar los íconos
        with st.container():
            # Distribuir en columnas para que se alineen horizontalmente
            col1, col2, col3, col4 = st.columns(4)

            # Ícono de Facebook
            with col1:
                st.markdown(
                    f'<a href="https://www.facebook.com" target="_blank">'
                    f'<img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="50"></a>',
                    unsafe_allow_html=True
                )

            # Ícono de Instagram
            with col2:
                st.markdown(
                    f'<a href="https://www.instagram.com" target="_blank">'
                    f'<img src="https://cdn-icons-png.flaticon.com/512/1409/1409946.png" width="50"></a>',
                    unsafe_allow_html=True
                )

            # Ícono de LinkedIn
            with col3:
                st.markdown(
                    f'<a href="https://www.linkedin.com" target="_blank">'
                    f'<img src="https://cdn-icons-png.flaticon.com/512/1409/1409945.png" width="50"></a>',
                    unsafe_allow_html=True
                )

            # Ícono de WhatsApp
            with col4:
                st.markdown(
                    f'<a href="https://wa.me/1234567890" target="_blank">'
                    f'<img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="50"></a>',
                    unsafe_allow_html=True
                )


















            #send(email,nombre,str(date),str(hora_seleccionada),servicio_seleccionado

            #create event in google calendar 
            
            #attendees = [email_empleado,email]
            #parsed_time = datetime.strptime(hora_seleccionada, "%H:%M").time()
            #start_time = datetime(date.year, date.month, date.day, parsed_time.hour, parsed_time.minute)
            #end_time = start_time + timedelta(minutes=30)

            #calendar_manager = GoogleCalendarManager()

            #calendar_manager.create_event(servicios+". "+nombre,start_time,end_time)

            #calendar_manager.create_event(servicio_seleccionado + ". " + nombre, start_time, end_time)
            #calendar_manager.create_event("Hola youtube","2024-12-08T16:30:00+02:00","2024-12-08T17:30:00+02:00","Europe/Madrid",["antonio@gmail.com","pedro@gmail.com"])


            #send email with confirm information
            

    # Pestaña Reseñas
    with tabs[1]:
        st.header("Reseñas")
        st.header("Lo que dicen nuestros clientes")
        st.markdown("""
⭐ ⭐ ⭐ ⭐ ⭐ *"El mejor taller mecánico en la ciudad. Mi camión quedó como nuevo. ¡Gracias CPK!"* — **Juan Pérez**

⭐ ⭐ ⭐ ⭐ ⭐ *"Repararon mi maquinaria pesada en tiempo récord. Excelente atención al detalle."* — **Ana Rodríguez**

⭐ ⭐ ⭐ ⭐ *"Buen servicio y precios competitivos. Volveré sin duda."* — **Carlos López**

⭐ ⭐ ⭐ ⭐ ⭐ *"Lo que más me gustó fue su transparencia al explicar los costos y las reparaciones necesarias."* — **Marta Gómez**
            """)
        st.text_input("¿Qué opinas de nuestros servicios? Déjanos tu reseña aquí:", key="reseña")
 

    # Pestaña Portafolio
    with tabs[2]:
        # sobre nosotros
        with st.container():
            st.write("---")
            left_column, right_column= st.columns((2))
            with left_column:
                st.header("Sobre nosotros")
                st.write(
                    """
                    En CPK, nos especializamos en ofrecer servicios de reparación y mantenimiento automotriz y Maquinarias de alta calidad, combinando profesionalismo, experiencia y tecnología avanzada para brindar soluciones eficientes a nuestros clientes.

Con más de 20 años de experiencia en el sector, nuestro equipo de mecánicos altamente capacitados está comprometido con la satisfacción del cliente, asegurando que cada vehículo reciba la atención y el cuidado que merece.

Nuestra Misión
Proporcionar un servicio técnico confiable, rápido y transparente que permita a nuestros clientes tener la tranquilidad de saber que su vehículo está en las mejores manos.

Nuestra Visión
Ser el taller mecánico líder en la región, reconocido por nuestra excelencia, innovación y atención personalizada.
                    """
                )


# Pestaña Detalles
    with tabs[3]:
        st.header("Detalles de Contacto")
        st.write("""
        - 📍 Dirección: Calle Abrebadero, nº5, chile 
        - 📞 Teléfono: +34 600 123 456
        - ✉️ Email: contacto@mecanico.com
                """)
    


        



#st.markdown(button, unsafe_allow_html=True)
#Falta Fecha, Servicio,horas disponibles, Empleado 

 




#registro

   # contact_form = f"""
    #<form action="https://formsubmit.co/{'email_address'}" method="POST">
     #   <input type="hidden" name="_captcha" value="false">
      #  <input type="text" name="name" placeholder="Tu nombre" required> 
      #  <input type="email" name="email" placeholder="Tu email" required>
      #  <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
      #  <button type="submit">Enviar</button>
 #  </form>


#    left_column, right_column = st.columns(2)
#   with left_column:
#       st.markdown(contact_form, unsafe_allow_html=True)
#   with right_column:
#       st.empty()
    


