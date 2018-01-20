#include <SoftwareSerial.h>
SoftwareSerial SIM900(18 , 19);

//global Variables

   char ManualLight[7]; //Manual light Proccessing 
   char MLval[4];  //Manual light Proccessing
   
   int MainDoor1= 23 ; //Main door pins (o/p)
   int MainDoor2= 24 ; //Main door pins (o/p)
   const long intervalPIR = 5000 ;
   int Buzzer= 11 ;//Buzzer pin (o/p)
   int OutLPin = 10 ; //Out Lights Pin
   


//Reception variables

  int RCPmlvalue ;
  bool RCPML = 0 ;
  int RCPLightPin = 2 ;  //light pin 
  int RCPLightMode = 0 ; //Light Mode 
  int rcpldr ; //Light sensor Reading
  int RCPLDR = A0 ; //LDR pin 
  int RCPintensity ; // intensity value by LDR

//Dining variables

  int DNmlvalue ;
  bool DNML = 0 ;
  int DNLightPin = 3 ;  //light pin
  int DNLightMode = 0 ; //Light Mode
  int dnldr ; //Light sensor Reading
  int DNLDR = A1 ; //LDR pin 
  int DNintensity ; // intensity value by LDR
  int DNWindow1 = 28 ;  //Window pin
  int DNWindow2 = 29 ;  //Window pin


//office variables

  int OFCmlvalue ;
  bool OFCML = 0 ;
  int OFCLightPin = 5 ;  //light pin 
  int OFCLightMode = 0 ; //Light Mode 
  int ofcldr ; //Light sensor Reading
  int OFCLDR = A2 ; //LDR pin 
  int OFCintensity ; // intensity value by LDR


//kitchen variables

 int KtnLightPin = 4 ;  //light pin 6 for kitchen
 bool GasLeakage ; //Gas Leakage Detection
 int GasSnsPin = 27 ; //Gas sensor Pin
 int GasValvePin = 48 ; //Gas Valve Pin
 bool GasSMS = 0 ;


//Room 1 Variables 

  int R1mlvalue ;
  bool R1security ; //EN. security 
  bool R1SecurityMode = 0 ; //Security Mode
  bool R1intrusion ; //intrusion status
  bool R1ML = 0 ; //En. Manual light
  int PIR = 30 ; // Motion sensor pin
  int R1photoIntr = 49 ; //Photo interrupter pin
  unsigned long previousMillisR1 = 0;
  
  int R1LightPin = 6 ;  //light pin 6 for room 1
  int R1EmergencyPin = 50 ; //Emergency Light pin 23 for room 1
  int R1LightMode = 0 ; //Light Mode room 1
  
  int r1ldr ; //Light sensor Reading
  int R1LDR = A3 ; //LDR pin 
  int R1intensity ; // intensity value by LDR
  bool IntrusionSMS = 0 ;

 


//Room 2 variables

  int R2mlvalue ;
  bool R2ML = 0 ;
  int R2LightPin = 7 ;  //light pin 
  int R2LightMode = 0 ; //Light Mode 
  int r2ldr ; //Light sensor Reading
  int R2LDR = A4 ; //LDR pin 
  int R2intensity ; // intensity value by LDR
  int R2Curtain1 = 39 ; //Curtain pin
  int R2Curtain2 = 40 ; //Curtain pin
  bool SmartCurtain = 0 ; 
  bool Curtain = 0 ; //Curtain Position
  int SCRLDR =  A8 ; //Smart Curtain LDR



//Room 3 variables

  int R3mlvalue ; 
  bool R3ML = 0 ;
  int R3LightPin = 8 ;  //light pin
  int R3LightMode = 0 ; //Light Mode
  int r3ldr ; //Light sensor Reading
  int R3LDR = A5 ; //LDR pin 
  int R3intensity ; // intensity value by LDR
  int R3Curtain1 = 41 ; //Curtain pin
  int R3Curtain2 = 42 ; //Curtain pin
  int R3Window1 = 43 ;  //Window pin
  int R3Window2 = 44 ;  //Window pin
  bool R3WState = 0 ;
  bool fire ; //Fire status
  int Smoke = 26 ; // Smoke sensor pin
  int FireValve = 47 ; //Fire Fight Valve pin
  int EmergencyLight1 = 22 ; //Emergency pin (o/p)
  int EmergencyLight2 = 25 ;
  bool Emergency ; //Emergyency status
  bool FireSMS = 0 ;
  

  

//Master bedroom variables

  int MRmlvalue ;
  bool MRML = 0 ;
  int MRLightPin = 9 ;  //light pin 
  int MRLightMode = 0 ; //Light Mode 
  int mrldr ; //Light sensor Reading
  int MRLDR = A6 ; //LDR pin 
  int MRintensity ; // intensity value by LDR



//Garage variables

    const long interval = 50000 ; // For time delay without hanging program
    unsigned long previousMillisGarage = 0;
    unsigned long currentMillis = 0;
    bool GarageOn = 0 ; //Open Or Close indicator
    int GaragePin1 = 45 ; //Garage pin
    int GaragePin2 = 46 ; //Garage pin
    bool GarageCase = 0 ;
   


//AC Remote Variables

    int AC1 = 31;
    int AC2 = 32;
    int AC5 = 33;
    int AC6 = 34;
    int AC7 = 35;
    int AC8 = 36;
    int AC9 = 37;
    int AC10 = 38 ;
    bool ACPower = 0 ;

//Temp Sensor 

int Temp ;
int TempSensor = A7 ;
const long TempInterval = 5000 ;
unsigned long previousMillisTemp = 0;

//Garden Light 
int GardenPin = 12 ;


String readString;

void setup() {
  Serial.begin(9600);
  
  SIM900.begin(19200);
  

  //OUT Light

  pinMode(OutLPin , OUTPUT);

  //Garden 

  pinMode(GardenPin , OUTPUT);
  

  //Main door
  pinMode(MainDoor1 , OUTPUT);
  pinMode(MainDoor2 , OUTPUT);

  //Reception

  pinMode(RCPLightPin , OUTPUT); 
  pinMode(RCPLDR ,INPUT );


  //Dining Room

  pinMode(DNLightPin , OUTPUT); 
  pinMode(DNLDR ,INPUT ); 
  pinMode(DNWindow1 , OUTPUT); 
  pinMode(DNWindow2 , OUTPUT); 

  //kitchen

  pinMode(KtnLightPin , OUTPUT);
  pinMode(GasSnsPin , INPUT );
  pinMode(GasValvePin , OUTPUT);

  //Office

  pinMode(OFCLightPin , OUTPUT); 
  pinMode(OFCLDR ,INPUT );


  //room 1 
  
  pinMode(PIR , INPUT); 
  pinMode(R1LightPin , OUTPUT); 
  pinMode(R1EmergencyPin , OUTPUT);   
  pinMode(R1LDR , INPUT);
  pinMode(R1photoIntr , INPUT);


  //room 2
  
  pinMode(R2LightPin , OUTPUT); 
  pinMode(R2LDR ,INPUT ); 
  pinMode(R2Curtain1 , OUTPUT); 
  pinMode(R2Curtain2 , OUTPUT); 
  pinMode(SCRLDR , INPUT) ;

  //room 3

  pinMode(EmergencyLight1 , OUTPUT );
  pinMode(EmergencyLight2 , OUTPUT );
  pinMode(R3LightPin , OUTPUT); 
  pinMode(R3LDR ,INPUT ); 
  pinMode(R3Curtain1 , OUTPUT); 
  pinMode(R3Curtain2 , OUTPUT); 
  pinMode(R3Window1 , OUTPUT); 
  pinMode(R3Window2 , OUTPUT); 
  pinMode(Smoke , INPUT);
  pinMode(FireValve , OUTPUT) ;
  pinMode(Buzzer , OUTPUT);


  //Master bedroom 

  pinMode(MRLightPin , OUTPUT); 
  pinMode(MRLDR ,INPUT ); 


  //Garage
   
   pinMode(GaragePin1 , OUTPUT );
   pinMode(GaragePin2 , OUTPUT );

   
  //AC Remote

  pinMode( AC1 , OUTPUT);
  pinMode( AC2 , OUTPUT);
  pinMode( AC5 , OUTPUT);
  pinMode( AC6 , OUTPUT);
  pinMode( AC7 , OUTPUT);
  pinMode( AC8 , OUTPUT);
  pinMode( AC9 , OUTPUT);
  pinMode( AC10 , OUTPUT);

  //----Temp Sensor-----//
  
  pinMode(TempSensor , INPUT);
 
  Serial.println("Smart Home"); 
}




void loop() {
currentMillis = millis();
  
  while (Serial.available()) {
    delay(3);  
    char c = Serial.read();
    readString += c; 
  }
  
  if (readString.length() >0) {
    

    // Manual intensity Control
    //--------------------------


    //--- Reception ----- //
    
    if( RCPML == 1 ){
      for (int i=0 ; i<6 ; i++){
        ManualLight[i]= readString[i];
      }
      ManualLight[6]='\0';
      
      if(strcmp(ManualLight , "RCPmlc")==0){
        for( int j=0 ; j<3 ; j++){
          MLval[j]= readString[j+6];
        }
        MLval[3]='\0' ;
        RCPmlvalue= ((MLval[0]-48)*100) +((MLval[1]-48)*10) +(MLval[2]-48) ;
        Serial.println(RCPmlvalue);
        
      }
    }


    //---- Office-----//

if( OFCML == 1 ){
      for (int i=0 ; i<6 ; i++){
        ManualLight[i]= readString[i];
      }
      ManualLight[6]='\0';
      
      if(strcmp(ManualLight , "OFCmlc")==0){
        for( int j=0 ; j<3 ; j++){
          MLval[j]= readString[j+6];
        }
        MLval[3]='\0' ;
        OFCmlvalue= ((MLval[0]-48)*100) +((MLval[1]-48)*10) +(MLval[2]-48) ;
        Serial.println(OFCmlvalue);
        
      }
    }

    //---- Dining Room ----//
    
    if( DNML == 1 ){
      for (int i=0 ; i<6 ; i++){
        ManualLight[i]= readString[i];
      }
      ManualLight[6]='\0';
      
      if(strcmp(ManualLight , "DN0mlc")==0){
        for( int j=0 ; j<3 ; j++){
          MLval[j]= readString[j+6];
        }
        MLval[3]='\0' ;
        DNmlvalue= ((MLval[0]-48)*100) +((MLval[1]-48)*10) +(MLval[2]-48) ;
        Serial.println(DNmlvalue);
        
      }
    }


    //--- Master BedRoom---//


    if( MRML ==1 ){
      for (int i=0 ; i<6 ; i++){
        ManualLight[i]= readString[i];
      }
      ManualLight[6]='\0';
      
      if(strcmp(ManualLight , "MR0mlc")==0){
        for( int j=0 ; j<3 ; j++){
          MLval[j]= readString[j+6];
        }
        MLval[3]='\0' ;
        MRmlvalue= ((MLval[0]-48)*100) +((MLval[1]-48)*10) +(MLval[2]-48) ;
        Serial.println(MRmlvalue);
        
      }
    }


    //--- Room 1 ---//

    
     if( R1ML == 1 ){
      for (int i=0 ; i<6 ; i++){
        ManualLight[i]= readString[i];
      }
      ManualLight[6]='\0';
      
      if(strcmp(ManualLight , "R01mlc")==0){
        for( int j=0 ; j<3 ; j++){
          MLval[j]= readString[j+6];
        }
        MLval[3]='\0' ;
        R1mlvalue= ((MLval[0]-48)*100) +((MLval[1]-48)*10) +(MLval[2]-48) ;
        Serial.println(R1mlvalue);
        
      }
    }


    //--- Room 2 ---//

     if( R2ML == 1 ){
      for (int i=0 ; i<6 ; i++){
        ManualLight[i]= readString[i];
      }
      ManualLight[6]='\0';
      
      if(strcmp(ManualLight , "R02mlc")==0){
        for( int j=0 ; j<3 ; j++){
          MLval[j]= readString[j+6];
        }
        MLval[3]='\0' ;
        R2mlvalue= ((MLval[0]-48)*100) +((MLval[1]-48)*10) +(MLval[2]-48) ;
        Serial.println(R2mlvalue);
        
      }
    }


    //--- Room 3---//

     if( R3ML == 1 ){
      for (int i=0 ; i<6 ; i++){
        ManualLight[i]= readString[i];
      }
      ManualLight[6]='\0';
      
      if(strcmp(ManualLight , "R03mlc")==0){
        for( int j=0 ; j<3 ; j++){
          MLval[j]= readString[j+6];
        }
        MLval[3]='\0' ;
        R3mlvalue= ((MLval[0]-48)*100) +((MLval[1]-48)*10) +(MLval[2]-48) ;
        Serial.println(R3mlvalue);
        
      }
    }


//-----------------End Of Manual Light ---------------//
//---------------------------------------------//

    
    



    //--------------------------------------------
                   //outer light
    //-------------------------------------------
     if (readString == "OUTLOn" ) {

      digitalWrite(OutLPin , HIGH);
      
     }
     if (readString == "OUTLOff") {

      digitalWrite(OutLPin , LOW);
      
     }
     
     //----------------------------------------------
                      //miandoor serials
    //-----------------------------------------------
                     

     if (readString == "OpenDoor") {
      
      digitalWrite(MainDoor1 , HIGH );
      digitalWrite(MainDoor2 , LOW ) ;
      delay(1400);
      digitalWrite(MainDoor1 , LOW );
      digitalWrite(MainDoor2 , LOW ) ;
      
    }

     if (readString == "CloseDoor") {
      
      digitalWrite(MainDoor1 , LOW );
      digitalWrite(MainDoor2 , HIGH ) ;
      delay(1400);
      digitalWrite(MainDoor1 , LOW );
      digitalWrite(MainDoor2 , LOW ) ;
      
    } 

//-------------- End Of Main door Serials --------------------------



    
    //-------------------------------------------------  
                     //Reception Serials
   //-------------------------------------------------



     //Reception Light Modes
 //------------------------------

        
    if (readString == "RCPLAOn"){
      RCPLightMode = 2 ;
      Serial.println("Reception Mode : Auto-On");
           
    }
    
    
    if (readString == "RCPLOn") {
      
      RCPLightMode = 0 ;
      Serial.println("Reception Mode : Full-On"); 
      digitalWrite(RCPLightPin , HIGH);
    }


    if (readString == "RCPLMOn") {
      RCPLightMode = 5 ;
      
      Serial.println("Reception Mode : Manual-On");
    }
   
    if (readString == "RCPLOff") {
      
      RCPLightMode = 0 ;
      Serial.println("Reception Mode : Off");
      digitalWrite(RCPLightPin, LOW);
    }

//-------------- End Of Reception Serials --------------------------

 
 
 //-------------------------------------------------  
                     //Dining Room Serials
   //-------------------------------------------------



     //Dining Room Light Modes
 //------------------------------

        
    if (readString == "DNLAOn"){
      DNLightMode = 2 ;
      Serial.println("Dining Room Mode : Auto-On");
           
    }
    
    
    if (readString == "DNLOn") {
      
      DNLightMode = 0 ;
      Serial.println("Dining Room Mode : Full-On"); 
      digitalWrite(DNLightPin , HIGH);
    }


    if (readString == "DNLMOn") {
      DNLightMode = 5 ;
      
      Serial.println("Dining Room Mode : Manual-On");
    }
   
    if (readString == "DNLOff") {
      
      DNLightMode = 0 ;
      Serial.println("Dining Room Mode : Off");
      digitalWrite(DNLightPin, LOW);
    }

     //Dining Room Window 
 //------------------------------

     if (readString == "DNWOpen") {
      
      digitalWrite(DNWindow1 , HIGH );
      digitalWrite(DNWindow2 , LOW ) ;
      delay(2500);
      digitalWrite(DNWindow1 , LOW );
      digitalWrite(DNWindow2 , LOW ) ;
      
    }

     if (readString == "DNWClose") {
      
      digitalWrite(DNWindow1 , LOW );
      digitalWrite(DNWindow2 , HIGH ) ;
      delay(2500);
      digitalWrite(DNWindow1 , LOW );
      digitalWrite(DNWindow2 , LOW ) ;
      
    } 

//-------------- End Of Dining Room Serials --------------------------



    //-------------------------------------------------  
                     //Kitchen Serials
    //-------------------------------------------------

        //---light---
        
       if (readString == "KtnLOn") {
        digitalWrite(KtnLightPin , HIGH );
       }
       if (readString == "KtnLOff") {
        digitalWrite(KtnLightPin , LOW );
       }

       //---Gas Leakage-----
       
        if (readString == "GasSecure") {
          GasLeakage = false ;
           Serial.println("GAS-Secured");
        }

 //-------------------------------------------------  
                     //Office Serials
   //-------------------------------------------------



     //Office Light Modes
 //------------------------------

        
    if (readString == "OFCLAOn"){
      OFCLightMode = 2 ;
      Serial.println("Office Mode : Auto-On");
           
    }
    
    
    if (readString == "OFCLOn") {
      
      OFCLightMode = 0 ;
      Serial.println("Office Mode : Full-On"); 
      digitalWrite(OFCLightPin , HIGH);
    }


    if (readString == "OFCLMOn") {
      OFCLightMode = 5 ;
      
      Serial.println("Office Mode : Manual-On");
    }
   
    if (readString == "OFCLOff") {
      
      OFCLightMode = 0 ;
      Serial.println("Office Mode : Off");
      digitalWrite(OFCLightPin, LOW);
    }

//-------------- End Of Office Serials --------------------------




  //-------------------------------------------------  
                     //Room No.1 Serials
  //------------------------------------------------- 

       //Room 1 Light Modes
 //------------------------------
       
    if (readString == "R1LAA"){
      R1LightMode = 1 ;
      Serial.println("Room 1 Mode : Auto-Auto");
      
    }
    
    if (readString == "R1LAOn"){
      R1LightMode = 2 ;
      Serial.println("Room 1 Mode : Auto-On");
           
    }
    
    if (readString == "R1LFA"){
      
      R1LightMode = 3 ;
      Serial.println("Room 1 Mode : Full-Auto");   
    }
    
    if (readString == "R1LOn") {
      
      R1LightMode = 0 ;
      Serial.println("Room 1 Mode : Full-On"); 
      digitalWrite(R1LightPin , HIGH);
    }

    if (readString == "R1LMA") {
      R1LightMode = 4 ;
      
      Serial.println("Room 1 Mode : Manual-Auto");   
    }

    if (readString == "R1LMOn") {
      R1LightMode = 5 ;
      
      Serial.println("Room 1 Mode : Manual-On");
      
    }
   
    if (readString == "R1LOff") {
      
      R1LightMode = 0 ;
      Serial.println("Room 1 Mode : Off");
      digitalWrite(R1LightPin, LOW);
    }

       

 
        //Room 1 Security 
//----------------------------


    if (readString == "R1SOne"){
      
      R1SecurityMode = 0 ;
      R1security = true ;
    }

    if (readString == "R1STwo"){
    
      R1SecurityMode = 1 ;
      R1security = true ;
    }

    if (readString == "R1SOff") {
      R1security = false ;
      digitalWrite( Buzzer , LOW ) ;
    }
    
    if (readString == "R1ALOff") {
       Serial.println("Alarm off");
       R1intrusion = false ;    
       digitalWrite(Buzzer , LOW);   
    }

    

    

//-------------- End Of Room 1 Serials --------------------------


//-------------------------------------------------  
                     //Room No.2 Serials
//-------------------------------------------------



     //Room 2 Light Modes
 //------------------------------

        
    if (readString == "R2LAOn"){
      R2LightMode = 2 ;
      Serial.println("Room 2 Mode : Auto-On");
           
    }
    
    
    if (readString == "R2LOn") {
      
      R2LightMode = 0 ;
      Serial.println("Room 2 Mode : Full-On"); 
      digitalWrite(R2LightPin , HIGH);
    }


    if (readString == "R2LMOn") {
      R2LightMode = 5 ;
      
      Serial.println("Room 2 Mode : Manual-On");
    }
   
    if (readString == "R2LOff") {
      
      R2LightMode = 0 ;
      Serial.println("Room 2 Mode : Off");
      digitalWrite(R2LightPin, LOW);
    }



       //Room 2 Curtain 
 //------------------------------

     if (readString == "R2CRSmart"){
      SmartCurtain = 1 ;
     }
     
     if (readString == "R2CROP") {

      SmartCurtain = 0 ;
      digitalWrite(R2Curtain1 , HIGH );
      digitalWrite(R2Curtain2 , LOW ) ;
      delay(5000);
      digitalWrite(R2Curtain1 , LOW );
      digitalWrite(R2Curtain2 , LOW ) ;
      Curtain = 1 ;
      
    }

     if (readString == "R2CRCL") {
      
      SmartCurtain = 0 ;
      digitalWrite(R2Curtain1 , LOW );
      digitalWrite(R2Curtain2 , HIGH ) ;
      delay(5000);
      digitalWrite(R2Curtain1 , LOW );
      digitalWrite(R2Curtain2 , LOW ) ;
      Curtain = 0 ;
    }

//-------------- End Of Room 2 Serials --------------------------



//-------------------------------------------------  
                     //Room No.3 Serials
//-------------------------------------------------



     //Room 3 Light Modes
 //------------------------------

        
    if (readString == "R3LAOn"){
      R3LightMode = 2 ;
      Serial.println("Room 3 Mode : Auto-On");
           
    }
    
    
    if (readString == "R3LOn") {
      
      R3LightMode = 0 ;
      Serial.println("Room 3 Mode : Full-On"); 
      digitalWrite(R3LightPin , HIGH);
    }


    if (readString == "R3LMOn") {
      R3LightMode = 5 ;
      
      Serial.println("Room 3 Mode : Manual-On");
    }
   
    if (readString == "R3LOff") {
      
      R3LightMode = 0 ;
      Serial.println("Room 3 Mode : Off");
      digitalWrite(R3LightPin, LOW);
    }



       //Room 3 Curtain 
 //------------------------------

     if (readString == "R3CROP") {
      
      Serial.println("Open curtain");
      
      digitalWrite(R3Curtain1 , HIGH );
      digitalWrite(R3Curtain2 , LOW ) ;
      delay(5000);
      digitalWrite(R3Curtain1 , LOW );
      digitalWrite(R3Curtain2 , LOW ) ;
      
    }

     if (readString == "R3CRCL") {
      
      digitalWrite(R3Curtain1 , LOW );
      digitalWrite(R3Curtain2 , HIGH ) ;
      delay(5000);
      digitalWrite(R3Curtain1 , LOW );
      digitalWrite(R3Curtain2 , LOW ) ;
      
    }

    //Room 3 Window 
 //------------------------------

     if (readString == "R3WOpen" && R3WState == 0) {
      
      digitalWrite(R3Window1 , HIGH );
      digitalWrite(R3Window2 , LOW ) ;
      delay(1600);
      digitalWrite(R3Window1 , LOW );
      digitalWrite(R3Window2 , LOW ) ;
      R3WState = 1 ;
    }

     if (readString == "R3WClose" && R3WState == 1) {
      
      digitalWrite(R3Window1 , LOW );
      digitalWrite(R3Window2 , HIGH ) ;
      delay(1600);
      digitalWrite(R3Window1 , LOW );
      digitalWrite(R3Window2 , LOW ) ;
      R3WState = 0 ;
    } 
    
    
       //Room 3 Fire
  //----------------------
        
     if (readString == "FireSecure") {
      fire = false ;
      digitalWrite(Buzzer , LOW);
      Serial.println("Fire-Secured");
    }
    
     if (readString == "EmergencyOff") {
      Emergency = false ;
      digitalWrite(Buzzer , LOW);
      Serial.println("Emergency-OFF");
    }

//-------------- End Of Room 3 Serials --------------------------


//-------------------------------------------------  
                     //Master bedroom Serials
//-------------------------------------------------



     //Master bedroom Light Modes
 //------------------------------

        
    if (readString == "MRLAOn"){
      MRLightMode = 2 ;
      Serial.println("Master bedroom Mode : Auto-On");
           
    }
    
    
    if (readString == "MRLOn") {
      
      MRLightMode = 0 ;
      Serial.println("Master bedroom Mode : Full-On"); 
      digitalWrite(MRLightPin , HIGH);
    }


    if (readString == "MRLMOn") {
      MRLightMode = 5 ;
      
      Serial.println("Master bedroom Mode : Manual-On");
    }
   
    if (readString == "MRLOff") {
      
      MRLightMode = 0 ;
      Serial.println("Master bedroom Mode : Off");
      digitalWrite(MRLightPin, LOW);
    }

//-------------- End Of Master bedroom Serials --------------------------


//-------------------------------------------------   
                     //Garage Serials
//-------------------------------------------------

    
    
     if ( ( readString == "OpenGarage" ) &&( GarageCase == 0 ) ) {

      GarageOn = 1 ;
      
      previousMillisGarage = currentMillis;
      digitalWrite(GaragePin1 , HIGH);
      digitalWrite(GaragePin2 , LOW);
      GarageCase = 1 ;
     

    }

     if ( (readString == "CloseGarage")  && ( GarageCase == 1) ) {

      GarageOn = 1 ;
     
      previousMillisGarage = currentMillis;
      digitalWrite(GaragePin1 , LOW);
      digitalWrite(GaragePin2 , HIGH);
      GarageCase = 0 ;

    }

    if ( readString == "StopGarage" ){
       GarageOn = 0 ;
        digitalWrite(GaragePin1 , LOW);
        digitalWrite(GaragePin2 , LOW);
       
    }
    
//-----------------End Of Garage Serials-------------------
    



   //----------------------AC Remote Serials---------------------------------//
   //-----------------------------------------------------------------------//
   
    
    if (  (readString == "ACPowerOn") && ( ACPower == 0) ) {
      digitalWrite(AC1 , HIGH);
      digitalWrite(AC5 , HIGH);
      delay(100);
      digitalWrite(AC1 , LOW);
      digitalWrite(AC5 , LOW);
      ACPower = 1 ;
      Serial.println("On");
     }

      if (  (readString == "ACPowerOff") && ( ACPower == 1) ) {
      digitalWrite(AC1 , HIGH);
      digitalWrite(AC5 , HIGH);
      delay(100);
      digitalWrite(AC1 , LOW);
      digitalWrite(AC5 , LOW);
      ACPower = 0 ;
      }

       if (  readString == "ACTempUp" ) {
      digitalWrite(AC1 , HIGH);
      digitalWrite(AC8 , HIGH);
      delay(100);
      digitalWrite(AC1 , LOW);
      digitalWrite(AC8 , LOW);
     }

     if (  readString == "ACTempDown" ) {
      digitalWrite(AC1 , HIGH);
      digitalWrite(AC6 , HIGH);
      delay(100);
      digitalWrite(AC1 , LOW);
      digitalWrite(AC6 , LOW);
     }

     if (  readString == "ACMode" ) {
      digitalWrite(AC2 , HIGH);
      digitalWrite(AC5 , HIGH);
      delay(100);
      digitalWrite(AC5 , LOW);
      digitalWrite(AC2 , LOW);
     }

     if (  readString == "ACFan" ) {
      digitalWrite(AC1 , HIGH);
      digitalWrite(AC7 , HIGH);
      delay(100);
      digitalWrite(AC1 , LOW);
      digitalWrite(AC7 , LOW);
     }

     if (  readString == "ACSwing" ) {
      digitalWrite(AC2 , HIGH);
      digitalWrite(AC7 , HIGH);
      delay(100);
      digitalWrite(AC2 , LOW);
      digitalWrite(AC7 , LOW);
     }

     if (  readString == "ACReset" ) {
      digitalWrite(AC9 , HIGH);
      digitalWrite(AC10 , HIGH);
      delay(100);
      digitalWrite(AC9 , LOW);
      digitalWrite(AC10 , LOW);
     }

     //--------------------------End Of AC Remote Serials--------------------------------//

     //---------Garden Serials------//

     if( readString == "Garden On"){
      
      digitalWrite(GardenPin , HIGH);
      
     }

     if( readString == "Garden Off"){

      digitalWrite(GardenPin , LOW);
      
     }

    
    }
    readString="";


//--------------------End Of Sreial Codes-------------------




    //------------Reception Codes ------------------//
    //-------------------------------------------//


          //Reception light Modes 
        //-----------------------------
   
          //Auto-On
          //-------
      
      if (RCPLightMode == 2){ 
        rcpldr = constrain(analogRead(RCPLDR) , 450 , 750);
      RCPintensity = map( rcpldr , 450 , 750 , 0 , 255 ); 
        analogWrite(RCPLightPin , RCPintensity); 
      }

      
           //Manual-On
           //---------

      if (RCPLightMode == 5){ 
        RCPML = 1 ;
        analogWrite(RCPLightPin , RCPmlvalue) ;
      }

//---------------End Of Reception codes----------------------




//------------Dining Room Codes ------------------//
    //-------------------------------------------//


          //Dining Room Modes 
        //-----------------------------
   
          //Auto-On
          //-------
      
      if (DNLightMode == 2){ 
        dnldr = constrain(analogRead(DNLDR) , 450 , 750);
      DNintensity = map( dnldr , 450 , 750 , 0 , 255 ); 
        analogWrite(DNLightPin , DNintensity); 
      }

      
           //Manual-On
           //---------

      if (DNLightMode == 5){ 
        DNML = 1 ;
        analogWrite(DNLightPin , DNmlvalue) ;
      }      

//---------------End Of Dining Room codes----------------------



 //------------Office Codes ------------------//
    //-------------------------------------------//


          //Office light Modes 
        //-----------------------------
   
          //Auto-On
          //-------
      
      if (OFCLightMode == 2){ 
        ofcldr = constrain(analogRead(OFCLDR) , 450 , 750);
      OFCintensity = map( ofcldr , 450 , 750 , 0 , 255 ); 
        analogWrite(OFCLightPin , OFCintensity); 
      }

      
           //Manual-On
           //---------

      if (OFCLightMode == 5){ 
        OFCML = 1 ;
        analogWrite(OFCLightPin , OFCmlvalue) ;
      }

//---------------End Of Office codes----------------------





    //------------Room 1 Codes ------------------//
    //-------------------------------------------//


          //Room 1 light Modes 
     //-----------------------------
     
         //Auto-Auto
         //---------
    
     if (R1LightMode == 1){   
      r1ldr = constrain(analogRead(R1LDR) , 200 , 700);
      R1intensity = map( r1ldr , 200 , 700 , 0 , 255 ); 
      if (digitalRead(PIR) == 1){
         previousMillisR1 =  currentMillis ;
        
      } 
      if (currentMillis - previousMillisR1 < intervalPIR){
         analogWrite(R1LightPin , R1intensity);
      }
      
       if (currentMillis - previousMillisR1 >= intervalPIR ){ 
          digitalWrite(R1LightPin , LOW);
       }
       
      
     
              
        
     }
     
          //Auto-On
          //-------
      
      if (R1LightMode == 2){ 
        r1ldr = constrain(analogRead(R1LDR) , 450 , 750);
      R1intensity = map( r1ldr , 450 , 750 , 0 , 255 ); 
        analogWrite(R1LightPin , R1intensity); 
      }

      
          //Full-Auto
          //----------
      
      if (R1LightMode == 3){
        if (digitalRead(PIR) == 1){    
          previousMillisR1 =  currentMillis ;
          digitalWrite(R1LightPin , HIGH); 
          
        }
       if (currentMillis - previousMillisR1 >= intervalPIR ){ 
          digitalWrite(R1LightPin , LOW);
              
        }
      }

      
           //Manual-Auto
           //-----------
           
      if (R1LightMode == 4){ 
        
        R1ML = 1 ;
        
        if(digitalRead(PIR) == 1){   
          previousMillisR1 =  currentMillis ;
        }
        if (currentMillis - previousMillisR1 < intervalPIR ){
         analogWrite( R1LightPin , R1mlvalue ); 
        }
        
        
        if (currentMillis - previousMillisR1 >= intervalPIR ){ 
          digitalWrite(R1LightPin , LOW);
              
        }
        
      }

      
           //Manual-On
           //---------

      if (R1LightMode == 5){ 

        R1ML = 1 ;
        
        analogWrite(R1LightPin , R1mlvalue) ;
      }
 

       // Room 1 Security Alarm 
     //--------------------------


     if ( IntrusionSMS == 1 ){
      
         IntrusionSMS = 0 ;
         SIM900.print("AT+CMGF=1\r");                                                        // AT command to send SMS message
        delay(100);
        SIM900.println("AT + CMGS = \"+201067555999\"");                                     // recipient's mobile number, in international format
        delay(100);
        SIM900.println("Intrusion At Room 1 ");        // message to send
        delay(100);
        SIM900.println((char)26);                       // End AT command with a ^Z, ASCII code 26
        delay(100); 
        SIM900.println();
        
        
       }
       
     if ( R1security == true && R1intrusion == false ){
      
      digitalWrite(R1EmergencyPin ,LOW);

       
      if ( R1SecurityMode == 1 ){
        if (digitalRead(PIR)== 1 || digitalRead(R1photoIntr) == 1){
         
        
          Serial.println("Intrusion Alarm");
          
          digitalWrite(R1EmergencyPin , HIGH);
          digitalWrite(Buzzer , HIGH);
          IntrusionSMS = 1; 
          R1intrusion = true ;  
            
        }
      }

      if ( R1SecurityMode == 0 ){
        if ( digitalRead(R1photoIntr) == 1){
          
          Serial.println("Intrusion Alarm");

          digitalWrite(R1EmergencyPin , HIGH);
          digitalWrite(Buzzer , HIGH);
          IntrusionSMS = 1 ;
          R1intrusion = true ;
        }
      }
     }
    
     
//---------------End Of Room 1 codes----------------------



    //------------Room 2 Codes ------------------//
    //-------------------------------------------//


          //Room 2 light Modes 
     //-----------------------------
   
          //Auto-On
          //-------
      
      if (R2LightMode == 2){ 
        r2ldr = constrain(analogRead(R2LDR) , 200 , 700);
      R2intensity = map( r2ldr , 200 , 700 , 0 , 255 ); 
        analogWrite(R2LightPin , R2intensity); 
      }

      
           //Manual-On
           //---------

      if (R2LightMode == 5){ 
        R2ML = 1 ;
        analogWrite(R2LightPin , R2mlvalue) ;
      }

      //-------------Smart Curtain --------//
      //----------------------------------//

      if( SmartCurtain == 1 ){

      if( (analogRead ( SCRLDR ) >= 900) && (Curtain == 1) ){

        digitalWrite(R2Curtain1 , LOW );
        digitalWrite(R2Curtain2 , HIGH ) ;
        delay(5000);
        digitalWrite(R2Curtain1 , LOW );
        digitalWrite(R2Curtain2 , LOW ) ;
        Curtain = 0 ;
      }
      
         if((analogRead ( SCRLDR ) < 900) && (Curtain == 0)){
  
          digitalWrite(R2Curtain1 , HIGH );
          digitalWrite(R2Curtain2 , LOW ) ;
          delay(5000);
          digitalWrite(R2Curtain1 , LOW );
          digitalWrite(R2Curtain2 , LOW ) ;
          Curtain = 1 ;
                
         }
        
      }

//---------------End Of Room 2 codes----------------------


    //------------Room 3 Codes ------------------//
    //-------------------------------------------//


          //Room 3 light Modes 
     //-----------------------------
   
          //Auto-On
          //-------
      
      if (R3LightMode == 2){ 
        r3ldr = constrain(analogRead(R3LDR) , 450 , 750);
      R3intensity = map( r3ldr , 450 , 750 , 0 , 255 ); 
        analogWrite(R3LightPin , R3intensity); 
      }

      
           //Manual-On
           //---------

      if (R3LightMode == 5){ 
        R3ML = 1 ;
        analogWrite(R3LightPin , R3mlvalue) ;
      }

            //Room 3 Smoke & Fire Alarm
 //----------------------------------------------

     if (fire == false) digitalWrite(FireValve , LOW);
     
     if (Emergency == false){
      digitalWrite(EmergencyLight1 , LOW);
      digitalWrite(EmergencyLight2 , LOW);
      
     }
     
     if ( fire == false && Emergency == false ){
        digitalWrite(FireValve , LOW);
        digitalWrite(EmergencyLight2 , LOW);
        digitalWrite(EmergencyLight1 , LOW);
        
          if ( digitalRead(Smoke) == 0){

            FireSMS=1 ;

            
            digitalWrite(FireValve , HIGH);
            digitalWrite(EmergencyLight2 , HIGH);
            digitalWrite(EmergencyLight1 , HIGH);
            digitalWrite(Buzzer , HIGH);

            
            
                   //open window
          if(R3WState = 0){
            digitalWrite(R3Window1 , HIGH );
            digitalWrite(R3Window2 , LOW ) ;
            delay(1600);
            digitalWrite(R3Window1 , LOW );
            digitalWrite(R3Window2 , LOW ) ;
          }
            
            fire = true ;
            Emergency = true ;
            Serial.println("Fire Alarm");
          }
     }

     if(FireSMS == 1 ){
            
             FireSMS = 0 ;
             SIM900.print("AT+CMGF=1\r");                                                        // AT command to send SMS message
             delay(100);
             SIM900.println("AT + CMGS = \"+201067555999\"");                                     // recipient's mobile number, in international format
              delay(100);
              SIM900.println("Fire At Room 3 ");        // message to send
              delay(100);
              SIM900.println((char)26);                       // End AT command with a ^Z, ASCII code 26
              delay(100); 
              SIM900.println();
              
             
          }

      

//---------------End Of Room 3 codes----------------------




 //------------Master bedroom Codes ------------------//
    //-------------------------------------------//


          //Master bedroom light Modes 
     //-----------------------------
   
          //Auto-On
          //-------
      
      if (MRLightMode == 2){ 
        mrldr = constrain(analogRead(MRLDR) , 450 , 750);
      MRintensity = map( mrldr , 450 , 750 , 0 , 255 ); 
        analogWrite(MRLightPin , MRintensity); 
      }

      
           //Manual-On
           //---------

      if (MRLightMode == 5){ 
        MRML = 1 ;
        analogWrite(MRLightPin , MRmlvalue) ;
      }

//---------------End Of Master bedroom codes----------------------




//------------------Garage Codes ----------------------//
//----------------------------------------------------//

 if ( GarageOn == 1 ){

      if ( (currentMillis - previousMillisGarage) >= interval ) {
        digitalWrite(GaragePin1 , LOW );
        digitalWrite(GaragePin2 , LOW );
        GarageOn= 0 ;
        
      }
     }
//------------------End Of Garage Codes---------------------

//------------------------------------------------------



      // GAS Leakage Alarm 
      
       if (GasLeakage == false){ 
        digitalWrite(GasValvePin , LOW);
          if ( digitalRead(GasSnsPin) == 0 ){

            GasSMS = true ;
            
           digitalWrite(GasValvePin , HIGH);
           GasLeakage = true ;
           Serial.println("GAS Leakage");
          }


       }

    if(GasSMS == 1 ){
            
             GasSMS = 0 ;
             SIM900.print("AT+CMGF=1\r");                                                        // AT command to send SMS message
             delay(100);
             SIM900.println("AT + CMGS = \"+201067555999\"");                                     // recipient's mobile number, in international format
              delay(100);
              SIM900.println("Gas Leakage At Kitchen ");        // message to send
              delay(100);
              SIM900.println((char)26);                       // End AT command with a ^Z, ASCII code 26
              delay(100); 
              SIM900.println();       
             
          }
//-----------------End Of GAS Leakage Alarm --------//
//-------------------------------------------------//



//-------------AC Remote Codes--------------------//
//------------------------------------------------//

if( (ACPower == 1) && (digitalRead(R1photoIntr) == 1)){
      digitalWrite(AC1 , HIGH);
      digitalWrite(AC5 , HIGH);
      delay(100);
      digitalWrite(AC1 , LOW);
      digitalWrite(AC5 , LOW);
      ACPower = 0 ;
    }
    
     //------Temperature Sensor Code ------//
     //-----------------------------------//
     
        if ( currentMillis - previousMillisTemp >= TempInterval ){
          Temp = analogRead(TempSensor);
          Serial.print("Temp");
          Serial.println(Temp-25);
          previousMillisTemp = currentMillis ;
        }

    


     
  } 
  
 
