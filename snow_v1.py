from bitstring import BitArray, BitStream

# -------------------------------------
# Funciones auxiliares:
def menor_32(x):
	aux=BitArray(length=32)
	if (len(x)<32):
		n=32-len(x)
		aux[n:]=x
		return aux
	else:
		return x

def listToString(l):
    string=""

    return (string.join(l))
# -------------------------------------

# Estados LFSR: 32bits
LFSR_S0=BitArray('0x00000000')
LFSR_S1=BitArray('0x00000000')
LFSR_S2=BitArray('0x00000000')
LFSR_S3=BitArray('0x00000000')
LFSR_S4=BitArray('0x00000000')
LFSR_S5=BitArray('0x00000000')
LFSR_S6=BitArray('0x00000000')
LFSR_S7=BitArray('0x00000000')
LFSR_S8=BitArray('0x00000000')
LFSR_S9=BitArray('0x00000000')
LFSR_S10=BitArray('0x00000000')
LFSR_S11=BitArray('0x00000000')
LFSR_S12=BitArray('0x00000000')
LFSR_S13=BitArray('0x00000000')
LFSR_S14=BitArray('0x00000000')
LFSR_S15=BitArray('0x00000000')


# Estados FSM: 32bits
FSM_R1=BitArray('0x00000000')
FSM_R2=BitArray('0x00000000')
FSM_R3=BitArray('0x00000000')

# S-box SR - 8bits 
SR=['0x63','0x7C','0x77','0x7B','0xF2','0x6B','0x6F','0xC5','0x30','0x01','0x67','0x2B','0xFE','0xD7','0xAB','0x76','0xCA','0x82','0xC9','0x7D','0xFA','0x59','0x47','0xF0','0xAD','0xD4','0xA2','0xAF','0x9C','0xA4','0x72','0xC0','0xB7','0xFD','0x93','0x26','0x36','0x3F','0xF7','0xCC','0x34','0xA5','0xE5','0xF1','0x71','0xD8','0x31','0x15','0x04','0xC7','0x23','0xC3','0x18','0x96','0x05','0x9A','0x07','0x12','0x80','0xE2','0xEB','0x27','0xB2','0x75','0x09','0x83','0x2C','0x1A','0x1B','0x6E','0x5A','0xA0','0x52','0x3B','0xD6','0xB3','0x29','0xE3','0x2F','0x84','0x53','0xD1','0x00','0xED','0x20','0xFC','0xB1','0x5B','0x6A','0xCB','0xBE','0x39','0x4A','0x4C','0x58','0xCF','0xD0','0xEF','0xAA','0xFB','0x43','0x4D','0x33','0x85','0x45','0xF9','0x02','0x7F','0x50','0x3C','0x9F','0xA8','0x51','0xA3','0x40','0x8F','0x92','0x9D','0x38','0xF5','0xBC','0xB6','0xDA','0x21','0x10','0xFF','0xF3','0xD2','0xCD','0x0C','0x13','0xEC','0x5F','0x97','0x44','0x17','0xC4','0xA7','0x7E','0x3D','0x64','0x5D','0x19','0x73','0x60','0x81','0x4F','0xDC','0x22','0x2A','0x90','0x88','0x46','0xEE','0xB8','0x14','0xDE','0x5E','0x0B','0xDB','0xE0','0x32','0x3A','0x0A','0x49','0x06','0x24','0x5C','0xC2','0xD3','0xAC','0x62','0x91','0x95','0xE4','0x79','0xE7','0xC8','0x37','0x6D','0x8D','0xD5','0x4E','0xA9','0x6C','0x56','0xF4','0xEA','0x65','0x7A','0xAE','0x08','0xBA','0x78','0x25','0x2E','0x1C','0xA6','0xB4','0xC6','0xE8','0xDD','0x74','0x1F','0x4B','0xBD','0x8B','0x8A','0x70','0x3E','0xB5','0x66','0x48','0x03','0xF6','0x0E','0x61','0x35','0x57','0xB9','0x86','0xC1','0x1D','0x9E','0xE1','0xF8','0x98','0x11','0x69','0xD9','0x8E','0x94','0x9B','0x1E','0x87','0xE9','0xCE','0x55','0x28','0xDF','0x8C','0xA1','0x89','0x0D','0xBF','0xE6','0x42','0x68','0x41','0x99','0x2D','0x0F','0xB0','0x54','0xBB','0x16']

# S-box SQ - 8bits
SQ=['0x25','0x24','0x73','0x67','0xD7','0xAE','0x5C','0x30','0xA4','0xEE','0x6E','0xCB','0x7D','0xB5','0x82','0xDB','0xE4','0x8E','0x48','0x49','0x4F','0x5D','0x6A','0x78','0x70','0x88','0xE8','0x5F','0x5E','0x84','0x65','0xE2','0xD8','0xE9','0xCC','0xED','0x40','0x2F','0x11','0x28','0x57','0xD2','0xAC','0xE3','0x4A','0x15','0x1B','0xB9','0xB2','0x80','0x85','0xA6','0x2E','0x02','0x47','0x29','0x07','0x4B','0x0E','0xC1','0x51','0xAA','0x89','0xD4','0xCA','0x01','0x46','0xB3','0xEF','0xDD','0x44','0x7B','0xC2','0x7F','0xBE','0xC3','0x9F','0x20','0x4C','0x64','0x83','0xA2','0x68','0x42','0x13','0xB4','0x41','0xCD','0xBA','0xC6','0xBB','0x6D','0x4D','0x71','0x21','0xF4','0x8D','0xB0','0xE5','0x93','0xFE','0x8F','0xE6','0xCF','0x43','0x45','0x31','0x22','0x37','0x36','0x96','0xFA','0xBC','0x0F','0x08','0x52','0x1D','0x55','0x1A','0xC5','0x4E','0x23','0x69','0x7A','0x92','0xFF','0x5B','0x5A','0xEB','0x9A','0x1C','0xA9','0xD1','0x7E','0x0D','0xFC','0x50','0x8A','0xB6','0x62','0xF5','0x0A','0xF8','0xDC','0x03','0x3C','0x0C','0x39','0xF1','0xB8','0xF3','0x3D','0xF2','0xD5','0x97','0x66','0x81','0x32','0xA0','0x00','0x06','0xCE','0xF6','0xEA','0xB7','0x17','0xF7','0x8C','0x79','0xD6','0xA7','0xBF','0x8B','0x3F','0x1F','0x53','0x63','0x75','0x35','0x2C','0x60','0xFD','0x27','0xD3','0x94','0xA5','0x7C','0xA1','0x05','0x58','0x2D','0xBD','0xD9','0xC7','0xAF','0x6B','0x54','0x0B','0xE0','0x38','0x04','0xC8','0x9D','0xE7','0x14','0xB1','0x87','0x9C','0xDF','0x6F','0xF9','0xDA','0x2A','0xC4','0x59','0x16','0x74','0x91','0xAB','0x26','0x61','0x76','0x34','0x2B','0xAD','0x99','0xFB','0x72','0xEC','0x33','0x12','0xDE','0x98','0x3B','0xC0','0x9B','0x3E','0x18','0x10','0x3A','0x56','0xE1','0x77','0xC9','0x1E','0x9E','0x95','0xA3','0x90','0x19','0xA8','0x6C','0x09','0xD0','0xF0','0x86']

# MULx funcion
# Descripcion: corresponde a la multiplicación con el elemento primitivo de grado 8 'beta',
# 			   siendo esta una raíz del polinomio irreducible x8 + c0x7 + c1x6 + c2x5 + c3x4 + c4x3 + c5x2 + c6x + c7. 
# 			   Quedando así: (V·B).
# Input V: 8bit
# Input c: 8bit
# Output: 8bit
def MULx(v,c):
	if v.bin[0]=='1':
		return ((v<<1)^c)
	else:
		return (v<<1)

# MULxPOW funcion
# Descripcion: corresponde a la multiplicación con el elemento 'beta' elevado a la potencia 'i'.
# Input V: 8bit
# Input i: int positivo
# Input c: 8bit
# Output: 8bit
def MULxPOW(v,i,c):
	if i==0:
		return v
	else:
		return MULx(MULxPOW(v,i-1,c),c)

# MULalpha funcion
# Descripcion: multiplicación del estado s0 por el elemento 'alfa'.
# Input c: 8bit
# Output: 32bit
def MULalpha(c):
	x=BitArray('0xa9')
	return ((MULxPOW(c,23,x))+(MULxPOW(c,245,x))+(MULxPOW(c,48,x))+(MULxPOW(c,239,x)))

# DIValpha funcion
# Descripcion: multiplicación del estado s11 por el inverso del elemento 'alfa'.
# Input c: 8bit
# Output: 32bit
def DIValpha(c):
	x=BitArray('0xa9')
	return ((MULxPOW(c,16,x))+(MULxPOW(c,39,x))+(MULxPOW(c,6,x))+(MULxPOW(c,64,x)))

# S1 box
# Descripcion: las S-box sirven para mapear y cambiar los bits entrantes aportando más seguridad al algoritmo.
# Input w: 32bit
# Output: 32bit
def S1(w):
	cte=BitArray('0x1b')

	srw0=SR[(w[:8]).uint]
	srw1=SR[(w[8:16]).uint]
	srw2=SR[(w[16:24]).uint]
	srw3=SR[(w[24:]).uint]

	srw0_new=BitArray(srw0)
	srw1_new=BitArray(srw1)
	srw2_new=BitArray(srw2)
	srw3_new=BitArray(srw3)

	r0=(MULx(srw0_new,cte)^(srw1_new)^(srw2_new)^(MULx(srw3_new,cte)^(srw3_new)))
	r1=((MULx(srw0_new,cte)^(srw0_new))^MULx(srw1_new,cte)^(srw2_new)^(srw3_new))
	r2=((srw0_new)^(MULx(srw1_new,cte)^(srw1_new))^MULx(srw2_new,cte)^(srw3_new))
	r3=((srw0_new)^(srw1_new)^(MULx(srw2_new,cte)^(srw2_new))^MULx(srw3_new,cte))

	return (r0+r1+r2+r3)

# S2 box
# Descripcion: las S-box sirven para mapear y cambiar los bits entrantes aportando más seguridad al algoritmo.
# Input w: 32bit
# Output: 32bit
def S2(w):
	cte=BitArray('0x69')

	sqw0=SQ[(w[:8]).uint]
	sqw1=SQ[(w[8:16]).uint]
	sqw2=SQ[(w[16:24]).uint]
	sqw3=SQ[(w[24:]).uint]

	sqw0_new=BitArray(sqw0)
	sqw1_new=BitArray(sqw1)
	sqw2_new=BitArray(sqw2)
	sqw3_new=BitArray(sqw3)

	r0=(MULx(sqw0_new,cte)^(sqw1_new)^(sqw2_new)^(MULx(sqw3_new,cte)^(sqw3_new)))
	r1=((MULx(sqw0_new,cte)^(sqw0_new))^MULx(sqw1_new,cte)^(sqw2_new)^(sqw3_new))
	r2=((sqw0_new)^(MULx(sqw1_new,cte)^(sqw1_new))^MULx(sqw2_new,cte)^(sqw3_new))
	r3=((sqw0_new)^(sqw1_new)^(MULx(sqw2_new,cte)^(sqw2_new))^MULx(sqw3_new,cte))

	return (r0+r1+r2+r3)

# Clocking LFSR in initialization mode
# Descripcion: Actualiza los valores del registro [s0-s15] en el modo inicialización.
# Input F: 32bit
def ClockLFSRInitializationMode(F):
	
	global LFSR_S0,LFSR_S1,LFSR_S2,LFSR_S3,LFSR_S4,LFSR_S5,LFSR_S6,LFSR_S7,LFSR_S8,LFSR_S9,LFSR_S10,LFSR_S11,LFSR_S12,LFSR_S13,LFSR_S14,LFSR_S15

	v=((LFSR_S0<<8)^MULalpha(BitArray(LFSR_S0[:8]))^(LFSR_S2)^(LFSR_S11>>8)^DIValpha(BitArray(LFSR_S11[24:]))^F)

	LFSR_S0=LFSR_S1
	LFSR_S1=LFSR_S2
	LFSR_S2=LFSR_S3
	LFSR_S3=LFSR_S4
	LFSR_S4=LFSR_S5
	LFSR_S5=LFSR_S6
	LFSR_S6=LFSR_S7
	LFSR_S7=LFSR_S8
	LFSR_S8=LFSR_S9
	LFSR_S9=LFSR_S10
	LFSR_S10=LFSR_S11
	LFSR_S11=LFSR_S12
	LFSR_S12=LFSR_S13
	LFSR_S13=LFSR_S14
	LFSR_S14=LFSR_S15
	LFSR_S15=v

# Clocking LFSR in keystream mode
# Descripcion: Actualiza los valores del registro [s0-s15] en el modo generación de clave.
def ClockLFSRKeyStreamMode():

	global LFSR_S0,LFSR_S1,LFSR_S2,LFSR_S3,LFSR_S4,LFSR_S5,LFSR_S6,LFSR_S7,LFSR_S8,LFSR_S9,LFSR_S10,LFSR_S11,LFSR_S12,LFSR_S13,LFSR_S14,LFSR_S15

	v=((LFSR_S0<<8)^MULalpha(BitArray(LFSR_S0[:8]))^(LFSR_S2)^(LFSR_S11>>8)^DIValpha(BitArray(LFSR_S11[24:])))

	LFSR_S0=LFSR_S1
	LFSR_S1=LFSR_S2
	LFSR_S2=LFSR_S3
	LFSR_S3=LFSR_S4
	LFSR_S4=LFSR_S5
	LFSR_S5=LFSR_S6
	LFSR_S6=LFSR_S7
	LFSR_S7=LFSR_S8
	LFSR_S8=LFSR_S9
	LFSR_S9=LFSR_S10	
	LFSR_S10=LFSR_S11
	LFSR_S11=LFSR_S12
	LFSR_S12=LFSR_S13
	LFSR_S13=LFSR_S14
	LFSR_S14=LFSR_S15
	LFSR_S15=v


# Clocking FSM
# Descripcion: actualiza los registros de la máquina de estados.
def ClockFSM():

	global FSM_R1, FSM_R2, FSM_R3, LFSR_S15, LFSR_S5

	# Calculo de F
	x=LFSR_S15.uint + FSM_R1.uint
	x%=4294967296
	y=menor_32(BitArray(hex(x))) & BitArray('0xffffffff')
	F=y ^ FSM_R2

	# Calculo de r
	a=FSM_R3 ^ LFSR_S5
	aux=FSM_R2.uint + a.uint
	aux%=4294967296
	r=menor_32(BitArray(hex(aux)))

	FSM_R3=S2(FSM_R2)
	FSM_R2=S1(FSM_R1)
	FSM_R1=r

	return F

# Initialization
# Descripcion: modo inicialización del algoritmo.
# Input k[4]: cuatro palabras de 32 bits formando una de 128-bit
# Input IV[4]: cuatro palabras de 32 bits formando una de 128-bit
def Initialize(k,IV):

	global LFSR_S0,LFSR_S1,LFSR_S2,LFSR_S3,LFSR_S4,LFSR_S5,LFSR_S6,LFSR_S7,LFSR_S8,LFSR_S9,LFSR_S10,LFSR_S11,LFSR_S12,LFSR_S13,LFSR_S14,LFSR_S15
	global FSM_R1, FSM_R2, FSM_R3

	LFSR_S15=k[3] ^ IV[0]
	LFSR_S14=k[2]
	LFSR_S13=k[1]
	LFSR_S12=k[0] ^ IV[1]

	LFSR_S11=k[3] ^ BitArray('0xffffffff')
	LFSR_S10=k[2] ^ BitArray('0xffffffff') ^ IV[2]
	LFSR_S9=k[1] ^ BitArray('0xffffffff') ^ IV[3]
	LFSR_S8=k[0] ^ BitArray('0xffffffff')

	LFSR_S7=k[3]
	LFSR_S6=k[2]
	LFSR_S5=k[1]
	LFSR_S4=k[0]

	LFSR_S3=k[3] ^ BitArray('0xffffffff')
	LFSR_S2=k[2] ^ BitArray('0xffffffff')
	LFSR_S1=k[1] ^ BitArray('0xffffffff')
	LFSR_S0=k[0] ^ BitArray('0xffffffff')

	FSM_R1=BitArray('0x00000000')
	FSM_R2=BitArray('0x00000000')
	FSM_R3=BitArray('0x00000000')

	for _ in range(32):
		F=ClockFSM()
		ClockLFSRInitializationMode(F)

# Generación de la clave
# Descripcion: modo generación de clave del algoritmo.
# Input n: número de palabras de 32 bits en la clave
# Output z: clave generada
def GenerateKeystream(n):
	ClockFSM()
	ClockLFSRKeyStreamMode()
	z=[]

	for _ in range(n):
		F=ClockFSM()
		z.append(F^LFSR_S0)
		ClockLFSRKeyStreamMode()
	return z

# ------------------------------------ #

# Main
# n=4
# k=[BitArray('0x8ce33e2c'),BitArray('0xc3c0b5fc'),BitArray('0x1f3de8a6'),BitArray('0xdc66b1f3')]
# IV=[BitArray('0xd3c5d592'),BitArray('0x327fb11c'),BitArray('0xde551988'),BitArray('0xceb2f9b7')]

# # k=[BitArray('0x4035c668'),BitArray('0x0af8c6d1'),BitArray('0xa8ff8667'),BitArray('0xb1714013')]
# # IV=[BitArray('0x62a54098'),BitArray('0x1ba6f9b7'),BitArray('0x4592b0e7'),BitArray('0x8690f71b')]

i=0
j=8
k=[]
iv=[]

print("Introduzca 'k': ")
x=input()

print("Introduzca 'IV': ")
y=input()

while j<=32:
    k.append(BitArray('0x'+x[i:j]))
    iv.append(BitArray('0x'+y[i:j]))
    i+=8
    j+=8

print("Introduzca modo de operación: ")
print("\t1.- Inicialización + Generación")
print("\t2.- Generación")
m=input()

print("Introduzca longitud de la secuencia: ")
n=int(input())

print("Nombre de fichero a guardar: ")
fich_name=input()

fich=open(fich_name,'a+')

def generation_mode(k,IV,n,m):
    if m=='1':
        Initialize(k,IV)
        keystream=GenerateKeystream(n)

        fich.write(listToString(str(keystream)))
        fich.write("\n")
        fich.close()
    elif m=='2':
        keystream=GenerateKeystream(n)

        fich.write(listToString(str(keystream)))
        fich.write("\n")
        fich.close()
    else:
        print("Valor incorrecto.")
        fich.close()
        exit()

generation_mode(k,iv,n,m)
