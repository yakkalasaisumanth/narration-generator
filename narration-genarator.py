from tkinter import *

root= Tk()
root.title("NARRATION GENERATOR")
root.geometry("500x500")
root.configure(bg='sky blue')

def EXIT():
	root.destroy()
	




def newwindow(text):
	entry.delete(0, END)
	entry.insert(0,text)
	global first
	first = entry.get()
	newwindow= Toplevel(root)
	newwindow.title("CASH")
	newwindow.geometry("500x500")
	newwindow.configure(bg="yellow")







	def mainmenu():
		newwindow.destroy()

	def on_click(text):
		e.delete(0, END)
		e.insert(0, text)
		global second
		second = e.get()
		if first == "CASH" and second == "SERVICE":
			service = Toplevel(newwindow)
			service.title("SERVICE")
			#service.configure(bg="yellow")

			def back():
				veh_no.delete(0, END)
				jc_no.delete(0, END)
				br_no.delete(0, END)
				loyality_points.delete(0, END)
				liability_date.delete(0, END)
				liability_amount.delete(0, END)
				liability_company.delete(0, END)
				advance_catagory.delete(0, END)
				advance_amount.delete(0, END)
				ph_no.delete(0, END)

				service.destroy()


			def SUBMIT():
				
				global a
				global b
				global c
				global d
				global e
				global f
				global g
				global h
				global i
				global g

				a = veh_no.get()
				b = jc_no.get()
				c = br_no.get()
				d = ph_no.get()
				e = liability_company.get()
				f = liability_date.get()
				g = liability_amount.get()
				h = advance_catagory.get()
				i = advance_amount.get()
				j = loyality_points.get()
				global cashwithoutliability
				cashwithoutliability = "BEING CASH RECEIVED TOWARDS VEH NO " + a + " JC NO " + b + " BR NO " + c + " PH NO " + d
				global liability
				liability = "INSURANCE COMPANY" + " " + e + " " +"DATE"+ " " + f + " " +"INSURANCE AMOUNT"+ " " + g
			



				if (len(liability) == 42):
					if(len(j) <= 0):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + additions.get()) 
						pass
					pass
				if(len(j) > 0):
					if(len(liability) == 42):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(i) > 0):
					if(len(liability) == 42):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) > 42):
					if(len(j) <= 0):
						if(len(i) <=0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + additions.get())
						pass
					pass
				if(len(liability)>42):
					if(len(j)>0):
						if(len(i) <= 0 ):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(i) >0):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(j) > 0):
						if(len(i) > 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				pass


				

			veh_no=Entry(service,width=40, borderwidth=5)
			veh_no.grid(row=0, column=1, padx=20, pady=10)
			jc_no= Entry(service,width=40, borderwidth=5)
			jc_no.grid(row=1, column=1, padx=20, pady=10)
			br_no= Entry(service,width=40, borderwidth=5)
			br_no.grid(row=2, column=1, padx=20, pady=10)
			ph_no= Entry(service,width=40, borderwidth=5)
			ph_no.grid(row=3, column=1, padx=20, pady=10)
			loyality_points= Entry(service,width=40, borderwidth=5)
			loyality_points.grid(row=4, column=1, padx=20, pady=10)
			liability_company= Entry(service,width=40, borderwidth=5)
			liability_company.grid(row=5, column=1, padx=20, pady=10)
			liability_date= Entry(service,width=40,borderwidth=5)
			liability_date.grid(row=6, column=1, padx=20, pady=10)
			liability_amount= Entry(service,width=40, borderwidth=5)
			liability_amount.grid(row=7, column=1, padx=20, pady=10)
			advance_catagory = Entry(service, width=40, borderwidth=5)
			advance_catagory.grid(row=8, column=1, padx=20, pady=10)
			advance_amount = Entry(service, width=40, borderwidth=5)
			advance_amount.grid(row=9, column=1, padx=20,pady=10)
			additions = Entry(service, width=40, borderwidth=5)
			additions.grid(row=10, column=1, padx=20,pady=10)
			button_1 = Button(service, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=11, column=0, columnspan=2)
			mybutton_2 = Button(service, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=12, column=0, columnspan=2)

			veh_no_label=Label(service, text="VEHICLE NUMBER")
			veh_no_label.grid(row=0, column=0)
			jc_no_label=Label(service, text="JOB CARD NUMBER")
			jc_no_label.grid(row=1, column=0)
			br_no_label=Label(service, text="BILL NUMBER")
			br_no_label.grid(row=2, column=0)
			ph_no_label=Label(service, text="PHONE NUMBER")
			ph_no_label.grid(row=3, column=0)
			loyality_no_label=Label(service, text="LOYALITY POINTS")
			loyality_no_label.grid(row=4, column=0)
			company_no_label=Label(service, text="LIABILITY COMPANY")
			company_no_label.grid(row=5, column=0)
			date_no_label=Label(service, text="LIABILITY DATE")
			date_no_label.grid(row=6, column=0)
			amount_no_label=Label(service, text="LIABILITY AMOUNT")
			amount_no_label.grid(row=7, column=0)
			advance_catagory_label = Label(service, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=8, column=0)
			advance_amount_label = Label(service, text="ADVANCE AMOUNT")
			advance_amount_label.grid(row=9, column=0)
			additions_label = Label(service, text="ADDITIONS IFANY")
			additions_label.grid(row=10, column=0)


		

		


		

		if first == "CASH" and second == "MDS":
			mds = Toplevel(newwindow)
			mds.title("MDS")

			def back():
				ph_no.delete(0, END)
				joning_amount.delete(0, END)
				part_amount.delete(0, END)
				final_amount.delete(0, END)
				class_extension.delete(0, END)
				crash_course.delete(0, END)
				mds.destroy()

			def SUBMIT():

				phone = ph_no.get()
				joining = joning_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				extenssion = class_extension.get()
				crash = crash_course.get()


				if(len(joining) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BEING CASH RECEIVED TOWARDS MDS JOINING AMOUNT " + "PH NO " + phone + " "  + additions.get())
								pass
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(joining) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BEING CASH RECEIVED TOWARDS MDS PART AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <= 0):
						if(len(joining) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BEING CASH RECEIVED TOWARDS MDS FINAL AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(extenssion) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(joining) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BEING CASH RECEIVED TOWARDS MDS CLASS EXTENSSION AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(crash) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(joining) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BEING CASH RECEIVED TOWARDS MDS CRASH COURSE AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				pass
				




			ph_no = Entry(mds, width=40,borderwidth=5)
			ph_no.grid(row=0, column=1,padx=20,pady=10)
			joning_amount = Entry(mds, width=40,borderwidth=5)
			joning_amount.grid(row=1, column=1,padx=20,pady=10)
			part_amount = Entry(mds, width=40,borderwidth=5)
			part_amount.grid(row=2, column=1,padx=20,pady=10)
			final_amount = Entry(mds, width=40,borderwidth=5)
			final_amount.grid(row=3, column=1,padx=20,pady=10)
			class_extension = Entry(mds, width=40,borderwidth=5)
			class_extension.grid(row=4, column=1,padx=20,pady=10)
			crash_course = Entry(mds, width=40,borderwidth=5)
			crash_course.grid(row=5, column=1,padx=20,pady=10)
			additions = Entry(mds, width=40,borderwidth=5)
			additions.grid(row=6, column=1,padx=20,pady=10)
			button_1 = Button(mds, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=7, column=0, columnspan=2)
			mybutton_2 = Button(mds, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=8, column=0, columnspan=2)


			ph_no_label=Label(mds,text="PHNOE NUMBER")
			ph_no_label.grid(row=0,column=0)
			joining_amount_label=Label(mds,text="JOINING AMOUNT")
			joining_amount_label.grid(row=1,column=0)
			part_amount_label=Label(mds,text="PART AMOUNT")
			part_amount_label.grid(row=2,column=0)
			final_amount_label=Label(mds,text="FINAL AMOUNT")
			final_amount_label.grid(row=3,column=0)
			class_extension_label=Label(mds,text="CLASS EXTENSSION")
			class_extension_label.grid(row=4,column=0)
			crash_cpuse_label=Label(mds,text="CRASH COURSE")
			crash_cpuse_label.grid(row=5,column=0)
			additions_label=Label(mds,text="ADDITIONS IFANY")
			additions_label.grid(row=6,column=0)


		

		

		if first == "CASH" and second == "INSURANCE":
			insurance = Toplevel(newwindow)
			insurance.title("insurance")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				renewal.delete(0, END)
				name_transfer.delete(0, END)
				insurance.destroy()

			def SUBMIT():

				ren = renewal.get()
				nt = name_transfer.get()

				if(len(ren) > 0):
					if(len(nt) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "BEING CASH RECEIVED TOWARDS INSURANCE RENEWAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " + additions.get())
					pass
				if(len(nt) > 0):
					if(len(ren) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "BEING CASH RECEIVED TOWARDS INSURANCE NAME TRANSFER AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " + additions.get())
					pass
				 






			veh_no = Entry(insurance, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(insurance, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			renewal = Entry(insurance, width=40, borderwidth=5)
			renewal.grid(row=2,column=1, padx=20,pady=10)
			name_transfer = Entry(insurance, width=40, borderwidth=5)
			name_transfer.grid(row=3,column=1, padx=20,pady=10)
			additions = Entry(insurance, width=40, borderwidth=5)
			additions.grid(row=4,column=1, padx=20,pady=10)
			button_1 = Button(insurance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=5, column=0, columnspan=2)
			mybutton_2 = Button(insurance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=6, column=0, columnspan=2)


			veh_no_label=Label(insurance, text="VEHICLE NUMBER")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(insurance, text="PHONE NUMBER")
			ph_no_label.grid(row=1, column=0)
			renewal_label=Label(insurance, text="RENEWAL AMOUNT")
			renewal_label.grid(row=2, column=0)
			name_transfer_label=Label(insurance, text="NAME TRANSFER")
			name_transfer_label.grid(row=3, column=0)
			additions_label=Label(insurance, text="ADDITIONS IFANY")
			additions_label.grid(row=4, column=0)

		

		

		

		


		if first == "CASH" and second == "NEW CAR":
			new_car = Toplevel(newwindow)
			new_car.title("NEW CAR")


			def back():
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				new_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CASH RECEIVED TOWARDS NEW CAR BOOKING AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CASH RECEIVED TOWARDS NEW CAR PART AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CASH RECEIVED TOWARDS NEW CAR FINAL AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CASH RECEIVED TOWARDS NEW CAR FINANCE AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				pass



			ph_no = Entry(new_car, width=40, borderwidth=5)
			ph_no.grid(row=0,column=1, padx=20,pady=10)
			veh_desc = Entry(new_car, width=40, borderwidth=5)
			veh_desc.grid(row=1,column=1, padx=20,pady=10)
			booking_amount = Entry(new_car, width=40, borderwidth=5)
			booking_amount.grid(row=2,column=1, padx=20,pady=10)
			part_amount = Entry(new_car, width=40, borderwidth=5)
			part_amount.grid(row=3,column=1, padx=20,pady=10)
			final_amount = Entry(new_car, width=40, borderwidth=5)
			final_amount.grid(row=4,column=1, padx=20,pady=10)
			finance_amount = Entry(new_car, width=40, borderwidth=5)
			finance_amount.grid(row=5,column=1, padx=20,pady=10)
			additions = Entry(new_car, width=40, borderwidth=5)
			additions.grid(row=6,column=1, padx=20,pady=10)
			button_1 = Button(new_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=8, column=0, columnspan=2)
			mybutton_2 = Button(new_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=9, column=0, columnspan=2)


			ph_no_label=Label(new_car, text="PHONE NUMBER")
			ph_no_label.grid(row=0, column=0)
			veh_desc_label=Label(new_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=1, column=0)
			booking_amount_label=Label(new_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=2, column=0)
			part_amount_label=Label(new_car, text="PART AMOUNT")
			part_amount_label.grid(row=3, column=0)
			final_amount_label=Label(new_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=4, column=0)
			finance_amount_label=Label(new_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=5, column=0)
			additions_label=Label(new_car, text="ADDITIONS IFANY")
			additions_label.grid(row=6, column=0)

		

		

		
		

		if first == "CASH" and second == "USED CAR":
			used_car = Toplevel(newwindow)
			used_car.title("USED CAR")


			def back():
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				used_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CASH RECEIVED TOWARDS USED CAR BOOKING AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CASH RECEIVED TOWARDS USED CAR PART AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CASH RECEIVED TOWARDS USED CAR FINAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CASH RECEIVED TOWARDS USED CAR FINANCE AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				pass



			veh_no = Entry(used_car, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(used_car, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			veh_price = Entry(used_car, width=40, borderwidth=5)
			veh_price.grid(row=2,column=1, padx=20,pady=10)
			veh_desc = Entry(used_car, width=40, borderwidth=5)
			veh_desc.grid(row=3,column=1, padx=20,pady=10)
			booking_amount = Entry(used_car, width=40, borderwidth=5)
			booking_amount.grid(row=4,column=1, padx=20,pady=10)
			part_amount = Entry(used_car, width=40, borderwidth=5)
			part_amount.grid(row=5,column=1, padx=20,pady=10)
			final_amount = Entry(used_car, width=40, borderwidth=5)
			final_amount.grid(row=6,column=1, padx=20,pady=10)
			finance_amount = Entry(used_car, width=40, borderwidth=5)
			finance_amount.grid(row=7,column=1, padx=20,pady=10)
			additions = Entry(used_car, width=40, borderwidth=5)
			additions.grid(row=8,column=1, padx=20,pady=10)
			button_1 = Button(used_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=9, column=0, columnspan=2)
			mybutton_2 = Button(used_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=10, column=0, columnspan=2)


			veh_no_label=Label(used_car, text="VEH NO")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(used_car, text="PHONE NUMBER")
			ph_no_label.grid(row=1, column=0)
			veh_price_label=Label(used_car, text="VEH PRICE")
			veh_price_label.grid(row=2, column=0)
			veh_desc_label=Label(used_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=3, column=0)
			booking_amount_label=Label(used_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=4, column=0)
			part_amount_label=Label(used_car, text="PART AMOUNT")
			part_amount_label.grid(row=5, column=0)
			final_amount_label=Label(used_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=6, column=0)
			finance_amount_label=Label(used_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=7, column=0)
			additions_label=Label(used_car, text="ADDITIONS IFANY")
			additions_label.grid(row=8, column=0)


		

		

		

		

		if first == "CASH"  and second == "ADVANCE":
			advance = Toplevel(newwindow)
			advance.title("ADVANCE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				advance_catagory.delete(0, END)
				additional_comment.delete(0, END)
				advance.destroy()


			def SUBMIT():
				text=Text(advance, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "BEING CASH RECEIVED TOWARDS " + advance_catagory.get() + " ADVANCE AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " +additional_comment.get())



			veh_no = Entry(advance, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(advance, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			advance_catagory = Entry(advance, width=40, borderwidth=5)
			advance_catagory.grid(row=2,column=1, padx=20,pady=10)
			additional_comment = Entry(advance, width=40, borderwidth=5)
			additional_comment.grid(row=3,column=1, padx=20,pady=10)
			button_1 = Button(advance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=4, column=0, columnspan=2)
			mybutton_2 = Button(advance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=5, column=0, columnspan=2)


			veh_no_label=Label(advance, text="VEH NO")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(advance, text="PHONE NO")
			ph_no_label.grid(row=1, column=0)
			advance_catagory_label=Label(advance, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=2, column=0)
			additional_comment_label=Label(advance, text="ADDITIONS IFANY")
			additional_comment_label.grid(row=3, column=0)

		

		

		

		

		if first == 'CASH' and second == 'COUNTER SALE':
			counter_sale = Toplevel(newwindow)
			counter_sale.title("COUNTER SALE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				invoice_no.delete(0, END)
				counter_sale.destroy()


			def SUBMIT():
				text=Text(counter_sale, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "BEING CASH RECEIVED TOWARDS COUNTER SALE FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " INVOICE NO " + invoice_no.get() + " " + additions.get())


			veh_no = Entry(counter_sale, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(counter_sale, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			invoice_no = Entry(counter_sale, width=40, borderwidth=5)
			invoice_no.grid(row=2,column=1, padx=20,pady=10)
			additions = Entry(counter_sale, width=40, borderwidth=5)
			additions.grid(row=3,column=1, padx=20,pady=10)
			button_1 = Button(counter_sale, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=4, column=0, columnspan=2)
			mybutton_2 = Button(counter_sale, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=5, column=0, columnspan=2)



			veh_no_label=Label(counter_sale, text="VEH NO/CUSTOMER NAME")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(counter_sale, text="PHONE NO")
			ph_no_label.grid(row=1, column=0)
			invoice_no_label=Label(counter_sale, text="INVOICE NO")
			invoice_no_label.grid(row=2, column=0)
			additions_label=Label(counter_sale, text="ADDITIONS IFANY")
			additions_label.grid(row=3, column=0)

		

		

		if first == "CASH" and second == "ACCESSORIES":
			accessories_sale = Toplevel(newwindow)
			accessories_sale.title("ACCESSORIES SALE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				obf_no.delete(0, END)
				accessories_sale.destroy()


			def SUBMIT():
				text=Text(accessories_sale, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "BEING CASH RECEIVED TOWARDS ACCESSORIES SALE FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " OBF/REFFERENCE NO " + obf_no.get() + " " + additions.get())


			veh_no = Entry(accessories_sale, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(accessories_sale, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			obf_no = Entry(accessories_sale, width=40, borderwidth=5)
			obf_no.grid(row=2,column=1, padx=20,pady=10)
			additions = Entry(accessories_sale, width=40, borderwidth=5)
			additions.grid(row=3,column=1, padx=20,pady=10)
			button_1 = Button(accessories_sale, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=4, column=0, columnspan=2)
			mybutton_2 = Button(accessories_sale, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=5, column=0, columnspan=2)



			veh_no_label=Label(accessories_sale, text="VEH NO/CUSTOMER NAME")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(accessories_sale, text="PHONE NO")
			ph_no_label.grid(row=1, column=0)
			obf_no_label=Label(accessories_sale, text="OBF/REF NO")
			obf_no_label.grid(row=2, column=0)
			additions_label=Label(accessories_sale, text="ADDITIONS IFANY")
			additions_label.grid(row=3, column=0)

		

		







		
		

	welcome_label=Label(newwindow, text="WELCOME TO NARRATION GENERATOR", fg ="green", font="poppins")
	welcome_label.grid(row=0, column=0 , columnspan=3)
	e = Entry(newwindow, width= 65)
	e.grid(row = 2, column=0, columnspan=3)
	mybutton_1 = Button(newwindow, text="SERVICE" ,padx=55, pady=20, command= lambda:on_click("SERVICE"),bg="#FF5B09", fg="black", borderwidth=4)
	mybutton_2 = Button(newwindow, text="MDS" ,padx=64, pady=20, command= lambda:on_click("MDS"),bg="#FFE303", fg="black", borderwidth=4)
	mybutton_3 = Button(newwindow, text="INSURANCE" ,padx=45, pady=20, command= lambda:on_click("INSURANCE"), bg="#AADD00", fg="black", borderwidth=4)

	mybutton_4 = Button(newwindow, text="NEW CAR" ,padx=50, pady=20, command= lambda:on_click("NEW CAR"), bg="#eedd82", fg="black", borderwidth=4)
	mybutton_5 = Button(newwindow, text="USED CAR" ,padx=50, pady=20, command= lambda:on_click("USED CAR"), bg="#82eedd", fg="black", borderwidth=4)
	mybutton_6 = Button(newwindow, text="ADVANCE" ,padx=50, pady=20, command= lambda:on_click("ADVANCE"), bg="#dd82ee", fg="black", borderwidth=4)

	mybutton_7 = Button(newwindow, text="COUNTER SALE" ,padx=36, pady=20, command= lambda:on_click("COUNTER SALE"),bg="#ffbf00", fg="black", borderwidth=4)
	mybutton_8 = Button(newwindow, text="ACCESSORIES" ,padx=42, pady=20, command= lambda:on_click("ACCESSORIES"), bg="#eea782", fg="black", borderwidth=4)
	mybutton_9 = Button(newwindow, text="BACK" ,padx=60, pady=20 , command=mainmenu , bg="#FF0000" , fg="black", borderwidth=4)


	mybutton_1.grid(row = 3, column=0)
	mybutton_2.grid(row = 3, column=1)
	mybutton_3.grid(row = 3, column=2)

	mybutton_4.grid(row = 4, column=0)
	mybutton_5.grid(row = 4, column=1)
	mybutton_6.grid(row = 4, column=2)

	mybutton_7.grid(row =5, column=0)
	mybutton_8.grid(row =5, column=1)
	mybutton_9.grid(row =5, column=2)

	welcome_label=Label(newwindow, text="CREATED BY", fg="green", font="poppins")
	welcome_label.grid(row=7, column=0 , columnspan=3)
	welcome_label=Label(newwindow, text="Y SAI SUMANTH", fg="green", font="poppins")
	welcome_label.grid(row=8, column=0 , columnspan=3)


def newwindow_1(text):
	entry.delete(0, END)
	entry.insert(0,text)
	global first
	first = entry.get()
	newwindow_1= Toplevel(root)
	newwindow_1.title("CARD")
	newwindow_1.geometry("500x500")
	newwindow_1.configure(bg="#FF8C00")







	def mainmenu():
		newwindow_1.destroy()

	def on_click(text):
		e.delete(0, END)
		e.insert(0, text)
		global second
		second = e.get()
		if first == "CARD" and second == "SERVICE":
			service = Toplevel(newwindow_1)
			service.title("CARD SERVICE")

			def back():
				veh_no.delete(0, END)
				jc_no.delete(0, END)
				br_no.delete(0, END)
				loyality_points.delete(0, END)
				liability_date.delete(0, END)
				liability_amount.delete(0, END)
				liability_company.delete(0, END)
				advance_catagory.delete(0, END)
				advance_amount.delete(0, END)
				ph_no.delete(0, END)

				service.destroy()


			def SUBMIT():
				
				global a
				global b
				global c
				global d
				global e
				global f
				global g
				global h
				global i
				global g

				a = veh_no.get()
				b = jc_no.get()
				c = br_no.get()
				d = ph_no.get()
				e = liability_company.get()
				f = liability_date.get()
				g = liability_amount.get()
				h = advance_catagory.get()
				i = advance_amount.get()
				j = loyality_points.get()
				global cashwithoutliability
				cashwithoutliability = "CARD AMOUNT RECEIVED TOWARDS VEH NO " + a + " JC NO " + b + " BR NO " + c + " PH NO " + d
				global liability
				liability = "INSURANCE COMPANY" + " " + e + " " +"DATE"+ " " + f + " " +"INSURANCE AMOUNT"+ " " + g
			



				if (len(liability) == 42):
					if(len(j) <= 0):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + additions.get()) 
						pass
					pass
				if(len(j) > 0):
					if(len(liability) == 42):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(i) > 0):
					if(len(liability) == 42):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) > 42):
					if(len(j) <= 0):
						if(len(i) <=0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + additions.get())
						pass
					pass
				if(len(liability)>42):
					if(len(j)>0):
						if(len(i) <= 0 ):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(liability)>42):
					if(len(i) >0):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(j) > 0):
						if(len(i) > 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				pass


				

			veh_no=Entry(service,width=40, borderwidth=5)
			veh_no.grid(row=0, column=1, padx=20, pady=10)
			jc_no= Entry(service,width=40, borderwidth=5)
			jc_no.grid(row=1, column=1, padx=20, pady=10)
			br_no= Entry(service,width=40, borderwidth=5)
			br_no.grid(row=2, column=1, padx=20, pady=10)
			ph_no= Entry(service,width=40, borderwidth=5)
			ph_no.grid(row=3, column=1, padx=20, pady=10)
			loyality_points= Entry(service,width=40, borderwidth=5)
			loyality_points.grid(row=4, column=1, padx=20, pady=10)
			liability_company= Entry(service,width=40, borderwidth=5)
			liability_company.grid(row=5, column=1, padx=20, pady=10)
			liability_date= Entry(service,width=40,borderwidth=5)
			liability_date.grid(row=6, column=1, padx=20, pady=10)
			liability_amount= Entry(service,width=40, borderwidth=5)
			liability_amount.grid(row=7, column=1, padx=20, pady=10)
			advance_catagory = Entry(service, width=40, borderwidth=5)
			advance_catagory.grid(row=8, column=1, padx=20, pady=10)
			advance_amount = Entry(service, width=40, borderwidth=5)
			advance_amount.grid(row=9, column=1, padx=20,pady=10)
			additions= Entry(service, width=40, borderwidth=5)
			additions.grid(row=10, column=1, padx=20,pady=10)
			button_1 = Button(service, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=11, column=0, columnspan=2)
			mybutton_2 = Button(service, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=12, column=0, columnspan=2)

			veh_no_label=Label(service, text="VEHICLE NUMBER")
			veh_no_label.grid(row=0, column=0)
			jc_no_label=Label(service, text="JOB CARD NUMBER")
			jc_no_label.grid(row=1, column=0)
			br_no_label=Label(service, text="BILL NUMBER")
			br_no_label.grid(row=2, column=0)
			ph_no_label=Label(service, text="PHONE NUMBER")
			ph_no_label.grid(row=3, column=0)
			loyality_no_label=Label(service, text="LOYALITY POINTS")
			loyality_no_label.grid(row=4, column=0)
			company_no_label=Label(service, text="LIABILITY COMPANY")
			company_no_label.grid(row=5, column=0)
			date_no_label=Label(service, text="LIABILITY DATE")
			date_no_label.grid(row=6, column=0)
			amount_no_label=Label(service, text="LIABILITY AMOUNT")
			amount_no_label.grid(row=7, column=0)
			advance_catagory_label = Label(service, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=8, column=0)
			advance_amount_label = Label(service, text="ADVANCE AMOUNT")
			advance_amount_label.grid(row=9, column=0)
			additions_label = Label(service, text="ADDITIONS IFANY")
			additions_label.grid(row=10, column=0)

		
		if first == "CARD" and second == "MDS":
			mds = Toplevel(newwindow_1)
			mds.title("CARD MDS")

			def back():
				ph_no.delete(0, END)
				joning_amount.delete(0, END)
				part_amount.delete(0, END)
				final_amount.delete(0, END)
				class_extension.delete(0, END)
				crash_course.delete(0, END)
				mds.destroy()

			def SUBMIT():

				phone = ph_no.get()
				joining = joning_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				extenssion = class_extension.get()
				crash = crash_course.get()


				if(len(joining) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "CARD AMOUNT RECEIVED TOWARDS MDS JOINING AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(joining) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "CARD AMOUNT RECEIVED TOWARDS MDS PART AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <= 0):
						if(len(joining) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "CARD AMOUNT RECEIVED TOWARDS MDS FINAL AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(extenssion) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(joining) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "CARD AMOUNT RECEIVED TOWARDS MDS CLASS EXTENSSION AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(crash) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(joining) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "CARD AMOUNT RECEIVED TOWARDS MDS CRASH COURSE AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				pass
				




			ph_no = Entry(mds, width=40,borderwidth=5)
			ph_no.grid(row=0, column=1,padx=20,pady=10)
			joning_amount = Entry(mds, width=40,borderwidth=5)
			joning_amount.grid(row=1, column=1,padx=20,pady=10)
			part_amount = Entry(mds, width=40,borderwidth=5)
			part_amount.grid(row=2, column=1,padx=20,pady=10)
			final_amount = Entry(mds, width=40,borderwidth=5)
			final_amount.grid(row=3, column=1,padx=20,pady=10)
			class_extension = Entry(mds, width=40,borderwidth=5)
			class_extension.grid(row=4, column=1,padx=20,pady=10)
			crash_course = Entry(mds, width=40,borderwidth=5)
			crash_course.grid(row=5, column=1,padx=20,pady=10)
			additions = Entry(mds, width=40,borderwidth=5)
			additions.grid(row=6, column=1,padx=20,pady=10)
			button_1 = Button(mds, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=7, column=0, columnspan=2)
			mybutton_2 = Button(mds, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=8, column=0, columnspan=2)


			ph_no_label=Label(mds,text="PHNOE NUMBER")
			ph_no_label.grid(row=0,column=0)
			joining_amount_label=Label(mds,text="JOINING AMOUNT")
			joining_amount_label.grid(row=1,column=0)
			part_amount_label=Label(mds,text="PART AMOUNT")
			part_amount_label.grid(row=2,column=0)
			final_amount_label=Label(mds,text="FINAL AMOUNT")
			final_amount_label.grid(row=3,column=0)
			class_extension_label=Label(mds,text="CLASS EXTENSSION")
			class_extension_label.grid(row=4,column=0)
			crash_cpuse_label=Label(mds,text="CRASH COURSE")
			crash_cpuse_label.grid(row=5,column=0)
			additions_label=Label(mds,text="ADDITIONS IFANY")
			additions_label.grid(row=6,column=0)

		if first == "CARD" and second == "INSURANCE":
			insurance = Toplevel(newwindow_1)
			insurance.title("CARD insurance")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				renewal.delete(0, END)
				name_transfer.delete(0, END)
				insurance.destroy()

			def SUBMIT():

				ren = renewal.get()
				nt = name_transfer.get()

				if(len(ren) > 0):
					if(len(nt) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "CARD AMOUNT RECEIVED TOWARDS INSURANCE RENEWAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " + additions.get())
					pass
				if(len(nt) > 0):
					if(len(ren) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "CARD AMOUNT RECEIVED TOWARDS INSURANCE NAME TRANSFER AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " + additions.get())
					pass
				 






			veh_no = Entry(insurance, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(insurance, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			renewal = Entry(insurance, width=40, borderwidth=5)
			renewal.grid(row=2,column=1, padx=20,pady=10)
			name_transfer = Entry(insurance, width=40, borderwidth=5)
			name_transfer.grid(row=3,column=1, padx=20,pady=10)
			additions = Entry(insurance, width=40, borderwidth=5)
			additions.grid(row=4,column=1, padx=20,pady=10)
			button_1 = Button(insurance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=5, column=0, columnspan=2)
			mybutton_2 = Button(insurance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=6, column=0, columnspan=2)


			veh_no_label=Label(insurance, text="VEHICLE NUMBER")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(insurance, text="PHONE NUMBER")
			ph_no_label.grid(row=1, column=0)
			renewal_label=Label(insurance, text="RENEWAL AMOUNT")
			renewal_label.grid(row=2, column=0)
			name_transfer_label=Label(insurance, text="NAME TRANSFER")
			name_transfer_label.grid(row=3, column=0)
			additions_label=Label(insurance, text="ADDITIONS IFANY")
			additions_label.grid(row=4, column=0)

		if first == "CARD" and second == "NEW CAR":
			new_car = Toplevel(newwindow_1)
			new_car.title("CARD NEW CAR")


			def back():
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				new_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "CARD AMOUNT RECEIVED TOWARDS NEW CAR BOOKING AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "CARD AMOUNT RECEIVED TOWARDS NEW CAR PART AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "CARD AMOUNT RECEIVED TOWARDS NEW CAR FINAL AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "CARD AMOUNT RECEIVED TOWARDS NEW CAR FINANCE AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				pass



			ph_no = Entry(new_car, width=40, borderwidth=5)
			ph_no.grid(row=0,column=1, padx=20,pady=10)
			veh_desc = Entry(new_car, width=40, borderwidth=5)
			veh_desc.grid(row=1,column=1, padx=20,pady=10)
			booking_amount = Entry(new_car, width=40, borderwidth=5)
			booking_amount.grid(row=2,column=1, padx=20,pady=10)
			part_amount = Entry(new_car, width=40, borderwidth=5)
			part_amount.grid(row=3,column=1, padx=20,pady=10)
			final_amount = Entry(new_car, width=40, borderwidth=5)
			final_amount.grid(row=4,column=1, padx=20,pady=10)
			finance_amount = Entry(new_car, width=40, borderwidth=5)
			finance_amount.grid(row=5,column=1, padx=20,pady=10)
			additions = Entry(new_car, width=40, borderwidth=5)
			additions.grid(row=6,column=1, padx=20,pady=10)
			button_1 = Button(new_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=8, column=0, columnspan=2)
			mybutton_2 = Button(new_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=9, column=0, columnspan=2)


			ph_no_label=Label(new_car, text="PHONE NUMBER")
			ph_no_label.grid(row=0, column=0)
			veh_desc_label=Label(new_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=1, column=0)
			booking_amount_label=Label(new_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=2, column=0)
			part_amount_label=Label(new_car, text="PART AMOUNT")
			part_amount_label.grid(row=3, column=0)
			final_amount_label=Label(new_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=4, column=0)
			finance_amount_label=Label(new_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=5, column=0)
			additions_label=Label(new_car, text="ADDITIONS IFANY")
			additions_label.grid(row=6, column=0)

		if first == "CARD" and second == "USED CAR":
			used_car = Toplevel(newwindow_1)
			used_car.title("CARD USED CAR")


			def back():
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0, END)
				used_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "CARD AMOUNT RECEIVED TOWARDS USED CAR BOOKING AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "CARD AMOUNT RECEIVED TOWARDS USED CAR PART AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "CARD AMOUNT RECEIVED TOWARDS USED CAR FINAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "CARD AMOUNT RECEIVED TOWARDS USED CAR FINANCE AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				pass



			veh_no = Entry(used_car, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(used_car, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			veh_price = Entry(used_car, width=40, borderwidth=5)
			veh_price.grid(row=2,column=1, padx=20,pady=10)
			veh_desc = Entry(used_car, width=40, borderwidth=5)
			veh_desc.grid(row=3,column=1, padx=20,pady=10)
			booking_amount = Entry(used_car, width=40, borderwidth=5)
			booking_amount.grid(row=4,column=1, padx=20,pady=10)
			part_amount = Entry(used_car, width=40, borderwidth=5)
			part_amount.grid(row=5,column=1, padx=20,pady=10)
			final_amount = Entry(used_car, width=40, borderwidth=5)
			final_amount.grid(row=6,column=1, padx=20,pady=10)
			finance_amount = Entry(used_car, width=40, borderwidth=5)
			finance_amount.grid(row=7,column=1, padx=20,pady=10)
			additions = Entry(used_car, width=40, borderwidth=5)
			additions.grid(row=8,column=1, padx=20,pady=10)
			button_1 = Button(used_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=9, column=0, columnspan=2)
			mybutton_2 = Button(used_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=10, column=0, columnspan=2)


			veh_no_label=Label(used_car, text="VEH NO")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(used_car, text="PHONE NUMBER")
			ph_no_label.grid(row=1, column=0)
			veh_price_label=Label(used_car, text="VEH PRICE")
			veh_price_label.grid(row=2, column=0)
			veh_desc_label=Label(used_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=3, column=0)
			booking_amount_label=Label(used_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=4, column=0)
			part_amount_label=Label(used_car, text="PART AMOUNT")
			part_amount_label.grid(row=5, column=0)
			final_amount_label=Label(used_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=6, column=0)
			finance_amount_label=Label(used_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=7, column=0)
			additions_label=Label(used_car, text="ADDITIONS IFANY")
			additions_label.grid(row=8, column=0)

		if first == "CARD"  and second == "ADVANCE":
			advance = Toplevel(newwindow_1)
			advance.title("CARD ADVANCE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				advance_catagory.delete(0, END)
				additional_comment.delete(0, END)
				advance.destroy()


			def SUBMIT():
				text=Text(advance, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "CARD AMOUNT RECEIVED TOWARDS " + advance_catagory.get() + " ADVANCE AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " + additional_comment.get())



			veh_no = Entry(advance, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(advance, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			advance_catagory = Entry(advance, width=40, borderwidth=5)
			advance_catagory.grid(row=2,column=1, padx=20,pady=10)
			additional_comment = Entry(advance, width=40, borderwidth=5)
			additional_comment.grid(row=3,column=1, padx=20,pady=10)
			button_1 = Button(advance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=4, column=0, columnspan=2)
			mybutton_2 = Button(advance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=5, column=0, columnspan=2)


			veh_no_label=Label(advance, text="VEH NO")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(advance, text="PHONE NO")
			ph_no_label.grid(row=1, column=0)
			advance_catagory_label=Label(advance, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=2, column=0)
			additional_comment_label=Label(advance, text="ADDITIONS IFANY")
			additional_comment_label.grid(row=3, column=0)

		if first == "CARD" and second == "ACCESSORIES":
			accessories_sale = Toplevel(newwindow_1)
			accessories_sale.title("CARD ACCESSORIES SALE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				obf_no.delete(0, END)
				accessories_sale.destroy()


			def SUBMIT():
				text=Text(accessories_sale, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "CARD AMOUNT RECEIVED TOWARDS ACCESSORIES SALE FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " OBF/REFFERENCE NO " + obf_no.get() + " " + additions.get())


			veh_no = Entry(accessories_sale, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(accessories_sale, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			obf_no = Entry(accessories_sale, width=40, borderwidth=5)
			obf_no.grid(row=2,column=1, padx=20,pady=10)
			additions = Entry(accessories_sale, width=40, borderwidth=5)
			additions.grid(row=3,column=1, padx=20,pady=10)
			button_1 = Button(accessories_sale, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=4, column=0, columnspan=2)
			mybutton_2 = Button(accessories_sale, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=5, column=0, columnspan=2)



			veh_no_label=Label(accessories_sale, text="VEH NO/CUSTOMER NAME")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(accessories_sale, text="PHONE NO")
			ph_no_label.grid(row=1, column=0)
			obf_no_label=Label(accessories_sale, text="OBF/REF NO")
			obf_no_label.grid(row=2, column=0)
			additions_label=Label(accessories_sale, text="ADDITIONS IFANY")
			additions_label.grid(row=3, column=0)

		if first == 'CARD' and second == 'COUNTER SALE':
			counter_sale = Toplevel(newwindow_1)
			counter_sale.title("CARD COUNTER SALE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				invoice_no.delete(0, END)
				counter_sale.destroy()


			def SUBMIT():
				text=Text(counter_sale, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "CARD AMOUNT RECEIVED TOWARDS COUNTER SALE FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " INVOICE NO " + invoice_no.get() + " " + additions.get())


			veh_no = Entry(counter_sale, width=40, borderwidth=5)
			veh_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(counter_sale, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			invoice_no = Entry(counter_sale, width=40, borderwidth=5)
			invoice_no.grid(row=2,column=1, padx=20,pady=10)
			additions = Entry(counter_sale, width=40, borderwidth=5)
			additions.grid(row=3,column=1, padx=20,pady=10)
			button_1 = Button(counter_sale, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=4, column=0, columnspan=2)
			mybutton_2 = Button(counter_sale, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=5, column=0, columnspan=2)



			veh_no_label=Label(counter_sale, text="VEH NO/CUSTOMER NAME")
			veh_no_label.grid(row=0, column=0)
			ph_no_label=Label(counter_sale, text="PHONE NO")
			ph_no_label.grid(row=1, column=0)
			invoice_no_label=Label(counter_sale, text="INVOICE NO")
			invoice_no_label.grid(row=2, column=0)
			additions_label=Label(counter_sale, text="ADDITIONS IFANY")
			additions_label.grid(row=3, column=0)

	welcome_label=Label(newwindow_1, text="WELCOME TO NARRATION GENERATOR", fg ="green", font="poppins")
	welcome_label.grid(row=0, column=0 , columnspan=3)
	e = Entry(newwindow_1, width= 65)
	e.grid(row = 2, column=0, columnspan=3)
	mybutton_1 = Button(newwindow_1, text="SERVICE" ,padx=55, pady=20, command= lambda:on_click("SERVICE"),bg="#FF5B09", fg="black", borderwidth=4)
	mybutton_2 = Button(newwindow_1, text="MDS" ,padx=64, pady=20, command= lambda:on_click("MDS"),bg="#FFE303", fg="black", borderwidth=4)
	mybutton_3 = Button(newwindow_1, text="INSURANCE" ,padx=45, pady=20, command= lambda:on_click("INSURANCE"), bg="#AADD00", fg="black", borderwidth=4)

	mybutton_4 = Button(newwindow_1, text="NEW CAR" ,padx=50, pady=20, command= lambda:on_click("NEW CAR"), bg="#eedd82", fg="black", borderwidth=4)
	mybutton_5 = Button(newwindow_1, text="USED CAR" ,padx=50, pady=20, command= lambda:on_click("USED CAR"), bg="#82eedd", fg="black", borderwidth=4)
	mybutton_6 = Button(newwindow_1, text="ADVANCE" ,padx=50, pady=20, command= lambda:on_click("ADVANCE"), bg="#dd82ee", fg="black", borderwidth=4)

	mybutton_7 = Button(newwindow_1, text="COUNTER SALE" ,padx=36, pady=20, command= lambda:on_click("COUNTER SALE"),bg="#ffbf00", fg="black", borderwidth=4)
	mybutton_8 = Button(newwindow_1, text="ACCESSORIES" ,padx=42, pady=20, command= lambda:on_click("ACCESSORIES"), bg="#eea782", fg="black", borderwidth=4)
	mybutton_9 = Button(newwindow_1, text="BACK" ,padx=60, pady=20 , command=mainmenu , bg="#FF0000" , fg="black", borderwidth=4)


	mybutton_1.grid(row = 3, column=0)
	mybutton_2.grid(row = 3, column=1)
	mybutton_3.grid(row = 3, column=2)

	mybutton_4.grid(row = 4, column=0)
	mybutton_5.grid(row = 4, column=1)
	mybutton_6.grid(row = 4, column=2)

	mybutton_7.grid(row =5, column=0)
	mybutton_8.grid(row =5, column=1)
	mybutton_9.grid(row =5, column=2)

	welcome_label=Label(newwindow_1, text="CREATED BY", fg="green", font="poppins")
	welcome_label.grid(row=7, column=0 , columnspan=3)
	welcome_label=Label(newwindow_1, text="Y SAI SUMANTH", fg="green", font="poppins")
	welcome_label.grid(row=8, column=0 , columnspan=3)


def newwindow_2(text):
	entry.delete(0, END)
	entry.insert(0,text)
	global first
	first = entry.get()
	newwindow_2= Toplevel(root)
	newwindow_2.title("BHIM")
	newwindow_2.geometry("500x500")
	newwindow_2.configure(bg="#BCEE68")







	def mainmenu():
		newwindow_2.destroy()

	def on_click(text):
		e.delete(0, END)
		e.insert(0, text)
		global second
		second = e.get()
		if first == "BHIM" and second == "SERVICE":
			service = Toplevel(newwindow_2)
			service.title("BHIM SERVICE")

			def back():
				bhim_upi.delete(0, END)
				veh_no.delete(0, END)
				jc_no.delete(0, END)
				br_no.delete(0, END)
				loyality_points.delete(0, END)
				liability_date.delete(0, END)
				liability_amount.delete(0, END)
				liability_company.delete(0, END)
				advance_catagory.delete(0, END)
				advance_amount.delete(0, END)
				ph_no.delete(0, END)

				service.destroy()


			def SUBMIT():
				
				global a
				global b
				global c
				global d
				global e
				global f
				global g
				global h
				global i
				global g

				a = veh_no.get()
				b = jc_no.get()
				c = br_no.get()
				d = ph_no.get()
				e = liability_company.get()
				f = liability_date.get()
				g = liability_amount.get()
				h = advance_catagory.get()
				i = advance_amount.get()
				j = loyality_points.get()
				global cashwithoutliability
				cashwithoutliability = "BHARAT BHIM UPI REF NO "  + bhim_upi.get() + " TOWARDS VEH NO "  + a + " JC NO " + b + " BR NO " + c + " PH NO " + d
				global liability
				liability = "INSURANCE COMPANY" + " " + e + " " +"DATE"+ " " + f + " " +"INSURANCE AMOUNT"+ " " + g
			



				if (len(liability) == 42):
					if(len(j) <= 0):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + additions.get()) 
						pass
					pass
				if(len(j) > 0):
					if(len(liability) == 42):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(i) > 0):
					if(len(liability) == 42):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) > 42):
					if(len(j) <= 0):
						if(len(i) <=0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + additions.get())
						pass
					pass
				if(len(liability)>42):
					if(len(j)>0):
						if(len(i) <= 0 ):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(i) >0):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + h + " ADVANCE AMOUNT " + i + " " +  additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(j) > 0):
						if(len(i) > 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				pass



			bhim_upi = Entry(service,width=40, borderwidth=5)	
			bhim_upi.grid(row= 0, column =1, padx=20, pady=10)	
			veh_no=Entry(service,width=40, borderwidth=5)
			veh_no.grid(row=1, column=1, padx=20, pady=10)
			jc_no= Entry(service,width=40, borderwidth=5)
			jc_no.grid(row=2, column=1, padx=20, pady=10)
			br_no= Entry(service,width=40, borderwidth=5)
			br_no.grid(row=3, column=1, padx=20, pady=10)
			ph_no= Entry(service,width=40, borderwidth=5)
			ph_no.grid(row=4, column=1, padx=20, pady=10)
			loyality_points= Entry(service,width=40, borderwidth=5)
			loyality_points.grid(row=5, column=1, padx=20, pady=10)
			liability_company= Entry(service,width=40, borderwidth=5)
			liability_company.grid(row=6, column=1, padx=20, pady=10)
			liability_date= Entry(service,width=40,borderwidth=5)
			liability_date.grid(row=7, column=1, padx=20, pady=10)
			liability_amount= Entry(service,width=40, borderwidth=5)
			liability_amount.grid(row=8, column=1, padx=20, pady=10)
			advance_catagory = Entry(service, width=40, borderwidth=5)
			advance_catagory.grid(row=9, column=1, padx=20, pady=10)
			advance_amount = Entry(service, width=40, borderwidth=5)
			advance_amount.grid(row=10, column=1, padx=20,pady=10)
			additions = Entry(service, width=40, borderwidth=5)
			additions.grid(row=11, column=1, padx=20,pady=10)
			button_1 = Button(service, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=12, column=0, columnspan=2)
			mybutton_2 = Button(service, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=13, column=0, columnspan=2)

			bhim_label=Label(service, text="UPI REF NUMBER")
			bhim_label.grid(row=0, column=0)
			veh_no_label=Label(service, text="VEHICLE NUMBER")
			veh_no_label.grid(row=1, column=0)
			jc_no_label=Label(service, text="JOB CARD NUMBER")
			jc_no_label.grid(row=2, column=0)
			br_no_label=Label(service, text="BILL NUMBER")
			br_no_label.grid(row=3, column=0)
			ph_no_label=Label(service, text="PHONE NUMBER")
			ph_no_label.grid(row=4, column=0)
			loyality_no_label=Label(service, text="LOYALITY POINTS")
			loyality_no_label.grid(row=5, column=0)
			company_no_label=Label(service, text="LIABILITY COMPANY")
			company_no_label.grid(row=6, column=0)
			date_no_label=Label(service, text="LIABILITY DATE")
			date_no_label.grid(row=7, column=0)
			amount_no_label=Label(service, text="LIABILITY AMOUNT")
			amount_no_label.grid(row=8, column=0)
			advance_catagory_label = Label(service, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=9, column=0)
			advance_amount_label = Label(service, text="ADVANCE AMOUNT")
			advance_amount_label.grid(row=10, column=0)
			additions_label = Label(service, text="ADDITIONS IFANY")
			additions_label.grid(row=11, column=0)

		if first == "BHIM" and second == "MDS":
			mds = Toplevel(newwindow_2)
			mds.title("BHIM MDS")

			def back():
				bhim_upi.delete(0, END)
				ph_no.delete(0, END)
				joning_amount.delete(0, END)
				part_amount.delete(0, END)
				final_amount.delete(0, END)
				class_extension.delete(0, END)
				crash_course.delete(0, END)
				mds.destroy()

			def SUBMIT():

				phone = ph_no.get()
				joining = joning_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				extenssion = class_extension.get()
				crash = crash_course.get()


				if(len(joining) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() +" TOWARDS MDS JOINING AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(joining) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() +" TOWARDS MDS PART AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <= 0):
						if(len(joining) <= 0):
							if(len(extenssion) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() +" TOWARDS MDS FINAL AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(extenssion) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(joining) <= 0):
								if(len(crash) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() +" TOWARDS MDS CLASS EXTENSSION AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				if(len(crash) > 0):
					if(len(part) <= 0):
						if(len(final) <= 0):
							if(len(extenssion) <= 0):
								if(len(joining) <= 0):
									text=Text(mds, width=40, height=6,padx=10,pady=10)
									text.grid(row=1, column=0, columnspan=2)
									text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() +" TOWARDS MDS CRASH COURSE AMOUNT " + "PH NO " + phone + " " + additions.get())
								pass
							pass
						pass
					pass
				pass
				




			bhim_upi = Entry(mds, width=40,borderwidth=5)
			bhim_upi.grid(row=0, column=1,padx=20,pady=10)
			ph_no = Entry(mds, width=40,borderwidth=5)
			ph_no.grid(row=1, column=1,padx=20,pady=10)
			joning_amount = Entry(mds, width=40,borderwidth=5)
			joning_amount.grid(row=2, column=1,padx=20,pady=10)
			part_amount = Entry(mds, width=40,borderwidth=5)
			part_amount.grid(row=3, column=1,padx=20,pady=10)
			final_amount = Entry(mds, width=40,borderwidth=5)
			final_amount.grid(row=4, column=1,padx=20,pady=10)
			class_extension = Entry(mds, width=40,borderwidth=5)
			class_extension.grid(row=5, column=1,padx=20,pady=10)
			crash_course = Entry(mds, width=40,borderwidth=5)
			crash_course.grid(row=6, column=1,padx=20,pady=10)
			additions = Entry(mds, width=40,borderwidth=5)
			additions.grid(row=7, column=1,padx=20,pady=10)
			button_1 = Button(mds, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=8, column=0, columnspan=2)
			mybutton_2 = Button(mds, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=9, column=0, columnspan=2)


			bhim_label=Label(mds,text="UPI REF NO")
			bhim_label.grid(row=0,column=0)
			ph_no_label=Label(mds,text="PHNOE NUMBER")
			ph_no_label.grid(row=1,column=0)
			joining_amount_label=Label(mds,text="JOINING AMOUNT")
			joining_amount_label.grid(row=2,column=0)
			part_amount_label=Label(mds,text="PART AMOUNT")
			part_amount_label.grid(row=3,column=0)
			final_amount_label=Label(mds,text="FINAL AMOUNT")
			final_amount_label.grid(row=4,column=0)
			class_extension_label=Label(mds,text="CLASS EXTENSSION")
			class_extension_label.grid(row=5,column=0)
			crash_cpuse_label=Label(mds,text="CRASH COURSE")
			crash_cpuse_label.grid(row=6,column=0)
			additions_label=Label(mds,text="ADDITIONS IFANY")
			additions_label.grid(row=7,column=0)

		if first == "BHIM" and second == "INSURANCE":
			insurance = Toplevel(newwindow_2)
			insurance.title("BHIM INSURANCE")

			def back():
				bhim_upi.delete(0,END)
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				renewal.delete(0, END)
				name_transfer.delete(0, END)
				bhim_upi.delete(0, END)
				insurance.destroy()

			def SUBMIT():

				ren = renewal.get()
				nt = name_transfer.get()

				if(len(ren) > 0):
					if(len(nt) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() +" TOWARDS INSURANCE RENEWAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " + additions.get())
					pass
				if(len(nt) > 0):
					if(len(ren) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() +" TOWARDS INSURANCE NAME TRANSFER AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " + additions.get())
					pass
				 






			bhim_upi = Entry(insurance, width=40, borderwidth=5)
			bhim_upi.grid(row=0,column=1, padx=20,pady=10)
			veh_no = Entry(insurance, width=40, borderwidth=5)
			veh_no.grid(row=1,column=1, padx=20,pady=10)
			ph_no = Entry(insurance, width=40, borderwidth=5)
			ph_no.grid(row=2,column=1, padx=20,pady=10)
			renewal = Entry(insurance, width=40, borderwidth=5)
			renewal.grid(row=3,column=1, padx=20,pady=10)
			name_transfer = Entry(insurance, width=40, borderwidth=5)
			name_transfer.grid(row=4,column=1, padx=20,pady=10)
			additions = Entry(insurance, width=40, borderwidth=5)
			additions.grid(row=5,column=1, padx=20,pady=10)
			button_1 = Button(insurance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=6, column=0, columnspan=2)
			mybutton_2 = Button(insurance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=7, column=0, columnspan=2)


			bhim_label=Label(insurance, text="UPI REF NUMBER")
			bhim_label.grid(row=0, column=0)
			veh_no_label=Label(insurance, text="VEHICLE NUMBER")
			veh_no_label.grid(row=1, column=0)
			ph_no_label=Label(insurance, text="PHONE NUMBER")
			ph_no_label.grid(row=2, column=0)
			renewal_label=Label(insurance, text="RENEWAL AMOUNT")
			renewal_label.grid(row=3, column=0)
			name_transfer_label=Label(insurance, text="NAME TRANSFER")
			name_transfer_label.grid(row=4, column=0)
			additions_label=Label(insurance, text="NAME TRANSFER")
			additions_label.grid(row=5, column=0)

		if first == "BHIM" and second == "NEW CAR":
			new_car = Toplevel(newwindow_2)
			new_car.title("BHIM NEW CAR")


			def back():
				bhim_upi.delete(0, END)
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				new_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + "  RECEIVED TOWARDS NEW CAR BOOKING AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + "  RECEIVED TOWARDS NEW CAR PART AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + "  RECEIVED TOWARDS NEW CAR FINAL AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + "  RECEIVED TOWARDS NEW CAR FINANCE AMOUNT FOR " + description + " PH NO " + phone + " " + additions.get())
							pass
						pass
					pass
				pass



			bhim_upi = Entry(new_car, width=40, borderwidth=5)
			bhim_upi.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(new_car, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			veh_desc = Entry(new_car, width=40, borderwidth=5)
			veh_desc.grid(row=2,column=1, padx=20,pady=10)
			booking_amount = Entry(new_car, width=40, borderwidth=5)
			booking_amount.grid(row=3,column=1, padx=20,pady=10)
			part_amount = Entry(new_car, width=40, borderwidth=5)
			part_amount.grid(row=4,column=1, padx=20,pady=10)
			final_amount = Entry(new_car, width=40, borderwidth=5)
			final_amount.grid(row=5,column=1, padx=20,pady=10)
			finance_amount = Entry(new_car, width=40, borderwidth=5)
			finance_amount.grid(row=6,column=1, padx=20,pady=10)
			additions = Entry(new_car, width=40, borderwidth=5)
			additions.grid(row=7,column=1, padx=20,pady=10)
			button_1 = Button(new_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=8, column=0, columnspan=2)
			mybutton_2 = Button(new_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=9, column=0, columnspan=2)


			bhim_label=Label(new_car, text="UPI REFFERENCE NO")
			bhim_label.grid(row=0, column=0)
			ph_no_label=Label(new_car, text="PHONE NUMBER")
			ph_no_label.grid(row=1, column=0)
			veh_desc_label=Label(new_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=2, column=0)
			booking_amount_label=Label(new_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=3, column=0)
			part_amount_label=Label(new_car, text="PART AMOUNT")
			part_amount_label.grid(row=4, column=0)
			final_amount_label=Label(new_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=5, column=0)
			finance_amount_label=Label(new_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=6, column=0)
			additions_label=Label(new_car, text="ADDITIONS IFANY")
			additions_label.grid(row=7, column=0)

		if first == "BHIM" and second == "USED CAR":
			used_car = Toplevel(newwindow_2)
			used_car.title("BHIM USED CAR")


			def back():
				bhim_upi.delete(0, END)
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				used_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + " TOWARDS USED CAR BOOKING AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + " TOWARDS USED CAR PART AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + " TOWARDS USED CAR FINAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + " TOWARDS USED CAR FINANCE AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " " + additions.get())
							pass
						pass
					pass
				pass



			bhim_upi = Entry(used_car, width=40, borderwidth=5)
			bhim_upi.grid(row=0,column=1, padx=20,pady=10)
			veh_no = Entry(used_car, width=40, borderwidth=5)
			veh_no.grid(row=1,column=1, padx=20,pady=10)
			ph_no = Entry(used_car, width=40, borderwidth=5)
			ph_no.grid(row=2,column=1, padx=20,pady=10)
			veh_price = Entry(used_car, width=40, borderwidth=5)
			veh_price.grid(row=3,column=1, padx=20,pady=10)
			veh_desc = Entry(used_car, width=40, borderwidth=5)
			veh_desc.grid(row=4,column=1, padx=20,pady=10)
			booking_amount = Entry(used_car, width=40, borderwidth=5)
			booking_amount.grid(row=5,column=1, padx=20,pady=10)
			part_amount = Entry(used_car, width=40, borderwidth=5)
			part_amount.grid(row=6,column=1, padx=20,pady=10)
			final_amount = Entry(used_car, width=40, borderwidth=5)
			final_amount.grid(row=7,column=1, padx=20,pady=10)
			finance_amount = Entry(used_car, width=40, borderwidth=5)
			finance_amount.grid(row=8,column=1, padx=20,pady=10)
			additions = Entry(used_car, width=40, borderwidth=5)
			additions.grid(row=9,column=1, padx=20,pady=10)
			button_1 = Button(used_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=10, column=0, columnspan=2)
			mybutton_2 = Button(used_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=11, column=0, columnspan=2)


			bhim_label=Label(used_car, text="UPI REF NO")
			bhim_label.grid(row=0, column=0)
			veh_no_label=Label(used_car, text="VEH NO")
			veh_no_label.grid(row=1, column=0)
			ph_no_label=Label(used_car, text="PHONE NUMBER")
			ph_no_label.grid(row=2, column=0)
			veh_price_label=Label(used_car, text="VEH PRICE")
			veh_price_label.grid(row=3, column=0)
			veh_desc_label=Label(used_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=4, column=0)
			booking_amount_label=Label(used_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=5, column=0)
			part_amount_label=Label(used_car, text="PART AMOUNT")
			part_amount_label.grid(row=6, column=0)
			final_amount_label=Label(used_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=7, column=0)
			finance_amount_label=Label(used_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=8, column=0)
			additions_label=Label(used_car, text="ADDITIONS IFANY")
			additions_label.grid(row=9, column=0)

		if first == "BHIM"  and second == "ADVANCE":
			advance = Toplevel(newwindow_2)
			advance.title("BHIM ADVANCE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				advance_catagory.delete(0, END)
				additional_comment.delete(0, END)
				advance.destroy()


			def SUBMIT():
				text=Text(advance, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + " TOWARDS " + advance_catagory.get() + " ADVANCE AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " +additional_comment.get())



			bhim_upi = Entry(advance, width=40, borderwidth=5)
			bhim_upi.grid(row=0,column=1, padx=20,pady=10)
			veh_no = Entry(advance, width=40, borderwidth=5)
			veh_no.grid(row=1,column=1, padx=20,pady=10)
			ph_no = Entry(advance, width=40, borderwidth=5)
			ph_no.grid(row=2,column=1, padx=20,pady=10)
			advance_catagory = Entry(advance, width=40, borderwidth=5)
			advance_catagory.grid(row=3,column=1, padx=20,pady=10)
			additional_comment = Entry(advance, width=40, borderwidth=5)
			additional_comment.grid(row=4,column=1, padx=20,pady=10)
			button_1 = Button(advance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=5, column=0, columnspan=2)
			mybutton_2 = Button(advance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=6, column=0, columnspan=2)


			bhim_label=Label(advance, text="UPI REF NO")
			bhim_label.grid(row=0, column=0)
			veh_no_label=Label(advance, text="VEH NO")
			veh_no_label.grid(row=1, column=0)
			ph_no_label=Label(advance, text="PHONE NO")
			ph_no_label.grid(row=2, column=0)
			advance_catagory_label=Label(advance, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=3, column=0)
			additional_comment_label=Label(advance, text="ADDITIONS IFANY")
			additional_comment_label.grid(row=4, column=0)

		if first == "BHIM" and second == "ACCESSORIES":
			accessories_sale = Toplevel(newwindow_2)
			accessories_sale.title("BHIM ACCESSORIES")

			def back():
				bhim_upi.delete(0, END)
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				obf_no.delete(0, END)
				accessories_sale.destroy()


			def SUBMIT():
				text=Text(accessories_sale, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "BHARAT BHIM UPI REF NO " +  bhim_upi.get() + " TOWARDS ACCESSORIES SALE FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " OBF/REFFERENCE NO " + obf_no.get() + " " + additions.get())


			bhim_upi = Entry(accessories_sale, width=40, borderwidth=5)
			bhim_upi.grid(row=0,column=1, padx=20,pady=10)
			veh_no = Entry(accessories_sale, width=40, borderwidth=5)
			veh_no.grid(row=1,column=1, padx=20,pady=10)
			ph_no = Entry(accessories_sale, width=40, borderwidth=5)
			ph_no.grid(row=2,column=1, padx=20,pady=10)
			obf_no = Entry(accessories_sale, width=40, borderwidth=5)
			obf_no.grid(row=3,column=1, padx=20,pady=10)
			additions = Entry(accessories_sale, width=40, borderwidth=5)
			additions.grid(row=4,column=1, padx=20,pady=10)
			button_1 = Button(accessories_sale, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=5, column=0, columnspan=2)
			mybutton_2 = Button(accessories_sale, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=6, column=0, columnspan=2)



			bhim_label=Label(accessories_sale, text="UPI REF NO")
			bhim_label.grid(row=0, column=0)
			veh_no_label=Label(accessories_sale, text="VEH NO/CUSTOMER NAME")
			veh_no_label.grid(row=1, column=0)
			ph_no_label=Label(accessories_sale, text="PHONE NO")
			ph_no_label.grid(row=2, column=0)
			obf_no_label=Label(accessories_sale, text="OBF/REF NO")
			obf_no_label.grid(row=3, column=0)
			additions_label=Label(accessories_sale, text="ADDITIONS IFANY")
			additions_label.grid(row=4, column=0)

		if first == 'BHIM' and second == 'COUNTER SALE':
			counter_sale = Toplevel(newwindow_2)
			counter_sale.title("BHIM COUNTER SALE")

			def back():
				bhim_upi.delete(0, END)
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				invoice_no.delete(0, END)
				counter_sale.destroy()


			def SUBMIT():
				text=Text(counter_sale, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "BHARAT BHIM UPI REF NO " + bhim_upi.get() + " TOWARDS COUNTER SALE FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " INVOICE NO " + invoice_no.get() + " " + additions.get())


			bhim_upi = Entry(counter_sale, width=40, borderwidth=5)
			bhim_upi.grid(row=0,column=1, padx=20,pady=10)
			veh_no = Entry(counter_sale, width=40, borderwidth=5)
			veh_no.grid(row=1,column=1, padx=20,pady=10)
			ph_no = Entry(counter_sale, width=40, borderwidth=5)
			ph_no.grid(row=2,column=1, padx=20,pady=10)
			invoice_no = Entry(counter_sale, width=40, borderwidth=5)
			invoice_no.grid(row=3,column=1, padx=20,pady=10)
			additions = Entry(counter_sale, width=40, borderwidth=5)
			additions.grid(row=4,column=1, padx=20,pady=10)
			button_1 = Button(counter_sale, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=5, column=0, columnspan=2)
			mybutton_2 = Button(counter_sale, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=6, column=0, columnspan=2)



			bhim_label=Label(counter_sale, text="UPI REF NO")
			bhim_label.grid(row=0, column=0)
			veh_no_label=Label(counter_sale, text="VEH NO/CUSTOMER NAME")
			veh_no_label.grid(row=1, column=0)
			ph_no_label=Label(counter_sale, text="PHONE NO")
			ph_no_label.grid(row=2, column=0)
			invoice_no_label=Label(counter_sale, text="INVOICE NO")
			invoice_no_label.grid(row=3, column=0)
			additions_label=Label(counter_sale, text="ADDITIONS IFANY")
			additions_label.grid(row=4, column=0)
	
	welcome_label=Label(newwindow_2, text="WELCOME TO NARRATION GENERATOR", fg ="green", font="poppins")
	welcome_label.grid(row=0, column=0 , columnspan=3)
	e = Entry(newwindow_2, width= 65)
	e.grid(row = 2, column=0, columnspan=3)
	mybutton_1 = Button(newwindow_2, text="SERVICE" ,padx=55, pady=20, command= lambda:on_click("SERVICE"),bg="#FF5B09", fg="black", borderwidth=4)
	mybutton_2 = Button(newwindow_2, text="MDS" ,padx=64, pady=20, command= lambda:on_click("MDS"),bg="#FFE303", fg="black", borderwidth=4)
	mybutton_3 = Button(newwindow_2, text="INSURANCE" ,padx=45, pady=20, command= lambda:on_click("INSURANCE"), bg="#AADD00", fg="black", borderwidth=4)

	mybutton_4 = Button(newwindow_2, text="NEW CAR" ,padx=50, pady=20, command= lambda:on_click("NEW CAR"), bg="#eedd82", fg="black", borderwidth=4)
	mybutton_5 = Button(newwindow_2, text="USED CAR" ,padx=50, pady=20, command= lambda:on_click("USED CAR"), bg="#82eedd", fg="black", borderwidth=4)
	mybutton_6 = Button(newwindow_2, text="ADVANCE" ,padx=50, pady=20, command= lambda:on_click("ADVANCE"), bg="#dd82ee", fg="black", borderwidth=4)

	mybutton_7 = Button(newwindow_2, text="COUNTER SALE" ,padx=36, pady=20, command= lambda:on_click("COUNTER SALE"),bg="#ffbf00", fg="black", borderwidth=4)
	mybutton_8 = Button(newwindow_2, text="ACCESSORIES" ,padx=42, pady=20, command= lambda:on_click("ACCESSORIES"), bg="#eea782", fg="black", borderwidth=4)
	mybutton_9 = Button(newwindow_2, text="BACK" ,padx=60, pady=20 , command=mainmenu , bg="#FF0000" , fg="black", borderwidth=4)


	mybutton_1.grid(row = 3, column=0)
	mybutton_2.grid(row = 3, column=1)
	mybutton_3.grid(row = 3, column=2)

	mybutton_4.grid(row = 4, column=0)
	mybutton_5.grid(row = 4, column=1)
	mybutton_6.grid(row = 4, column=2)

	mybutton_7.grid(row =5, column=0)
	mybutton_8.grid(row =5, column=1)
	mybutton_9.grid(row =5, column=2)

	welcome_label=Label(newwindow_2, text="CREATED BY", fg="sky blue", font="poppins")
	welcome_label.grid(row=7, column=0 , columnspan=3)
	welcome_label=Label(newwindow_2, text="Y SAI SUMANTH", fg="sky blue", font="poppins")
	welcome_label.grid(row=8, column=0 , columnspan=3)

def newwindow_3(text):
	entry.delete(0, END)
	entry.insert(0,text)
	global first
	first = entry.get()
	newwindow_3= Toplevel(root)
	newwindow_3.title("ONLINE")
	newwindow_3.geometry("500x500")
	newwindow_3.configure(bg="#1E90FF")







	def mainmenu():
		newwindow_3.destroy()

	def on_click(text):
		e.delete(0, END)
		e.insert(0, text)
		global second
		second = e.get()
		if first == "ONLINE" and second == "SERVICE":
			service = Toplevel(newwindow_3)
			service.title("ONLINE SERVICE")

			def back():
				on_date.delete(0,END)
				bank_name.delete(0, END)
				online_ref.delete(0, END)
				veh_no.delete(0, END)
				jc_no.delete(0, END)
				br_no.delete(0, END)
				loyality_points.delete(0, END)
				liability_date.delete(0, END)
				liability_amount.delete(0, END)
				liability_company.delete(0, END)
				advance_catagory.delete(0, END)
				advance_amount.delete(0, END)
				ph_no.delete(0, END)

				service.destroy()


			def SUBMIT():
				
				global a
				global b
				global c
				global d
				global e
				global f
				global g
				global h
				global i
				global g

				a = veh_no.get()
				b = jc_no.get()
				c = br_no.get()
				d = ph_no.get()
				e = liability_company.get()
				f = liability_date.get()
				g = liability_amount.get()
				h = advance_catagory.get()
				i = advance_amount.get()
				j = loyality_points.get()
				global cashwithoutliability
				cashwithoutliability = "BEING ONLINE AMOUNT CREDITED IN "  + bank_name.get() + " ON DATE "  + on_date.get() + a + " JC NO " + b + " BR NO " + c + " PH NO " + d + " REFFERENCE NUMBER " + online_ref.get()
				global liability
				liability = "INSURANCE COMPANY" + " " + e + " " +"DATE"+ " " + f + " " +"INSURANCE AMOUNT"+ " " + g
			



				if (len(liability) == 42):
					if(len(j) <= 0):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + additions.get()) 
						pass
					pass
				if(len(j) > 0):
					if(len(liability) == 42):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(i) > 0):
					if(len(liability) == 42):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) > 42):
					if(len(j) <= 0):
						if(len(i) <=0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + additions.get())
						pass
					pass
				if(len(liability)>42):
					if(len(j)>0):
						if(len(i) <= 0 ):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(i) >0):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(j) > 0):
						if(len(i) > 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				pass



			online_ref = Entry(service,width=40, borderwidth=5)	
			online_ref.grid(row= 0, column =1, padx=20, pady=10)
			bank_name = Entry(service,width=40, borderwidth=5)	
			bank_name.grid(row= 1, column =1, padx=20, pady=10)
			on_date=Entry(service,width=40, borderwidth=5)
			on_date.grid(row=2, column=1, padx=20, pady=10)	
			veh_no=Entry(service,width=40, borderwidth=5)
			veh_no.grid(row=3, column=1, padx=20, pady=10)
			jc_no= Entry(service,width=40, borderwidth=5)
			jc_no.grid(row=4, column=1, padx=20, pady=10)
			br_no= Entry(service,width=40, borderwidth=5)
			br_no.grid(row=5, column=1, padx=20, pady=10)
			ph_no= Entry(service,width=40, borderwidth=5)
			ph_no.grid(row=6, column=1, padx=20, pady=10)
			loyality_points= Entry(service,width=40, borderwidth=5)
			loyality_points.grid(row=7, column=1, padx=20, pady=10)
			liability_company= Entry(service,width=40, borderwidth=5)
			liability_company.grid(row=8, column=1, padx=20, pady=10)
			liability_date= Entry(service,width=40,borderwidth=5)
			liability_date.grid(row=9, column=1, padx=20, pady=10)
			liability_amount= Entry(service,width=40, borderwidth=5)
			liability_amount.grid(row=10, column=1, padx=20, pady=10)
			advance_catagory = Entry(service, width=40, borderwidth=5)
			advance_catagory.grid(row=11, column=1, padx=20, pady=10)
			advance_amount = Entry(service, width=40, borderwidth=5)
			advance_amount.grid(row=12, column=1, padx=20,pady=10)
			additions = Entry(service, width=40, borderwidth=5)
			additions.grid(row=13, column=1, padx=20,pady=10)
			button_1 = Button(service, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=14, column=0, columnspan=2)
			mybutton_2 = Button(service, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=15, column=0, columnspan=2)

			online_label=Label(service, text="ONLINE REF NO")
			online_label.grid(row=0, column=0)
			bank_name_label=Label(service, text="BANK ACCOUNT NAME")
			bank_name_label.grid(row=1, column=0)
			on_date_label=Label(service, text="ON DATE")
			on_date_label.grid(row=2, column=0)
			veh_no_label=Label(service, text="VEHICLE NUMBER")
			veh_no_label.grid(row=3, column=0)
			jc_no_label=Label(service, text="JOB CARD NUMBER")
			jc_no_label.grid(row=4, column=0)
			br_no_label=Label(service, text="BILL NUMBER")
			br_no_label.grid(row=5, column=0)
			ph_no_label=Label(service, text="PHONE NUMBER")
			ph_no_label.grid(row=6, column=0)
			loyality_no_label=Label(service, text="LOYALITY POINTS")
			loyality_no_label.grid(row=7, column=0)
			company_no_label=Label(service, text="LIABILITY COMPANY")
			company_no_label.grid(row=8, column=0)
			date_no_label=Label(service, text="LIABILITY DATE")
			date_no_label.grid(row=9, column=0)
			amount_no_label=Label(service, text="LIABILITY AMOUNT")
			amount_no_label.grid(row=10, column=0)
			advance_catagory_label = Label(service, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=11, column=0)
			advance_amount_label = Label(service, text="ADVANCE AMOUNT")
			advance_amount_label.grid(row=12, column=0)
			additions_label = Label(service, text="ADDITIONS IFANY")
			additions_label.grid(row=13, column=0)

		if first == "ONLINE" and second == "INSURANCE":
			insurance = Toplevel(newwindow_3)
			insurance.title("ONLINE INSURANCE")

			def back():
				online_ref.delete(0, END)
				on_date.delete(0, END)
				bank_name.delete(0, END)
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				renewal.delete(0, END)
				name_transfer.delete(0, END)
				insurance.destroy()

			def SUBMIT():

				ren = renewal.get()
				nt = name_transfer.get()

				if(len(ren) > 0):
					if(len(nt) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " ON DATE " + on_date.get() + " TOWARDS INSURANCE RENEWAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " REFFERENCE NO " + online_ref.get() + " " + additions.get()) 
					pass
				if(len(nt) > 0):
					if(len(ren) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " ON DATE " + on_date.get() + " TOWARDS INSURANCE NAME TRANSFER AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " REFFERENCE NO " + online_ref.get() + " " + additions.get())
					pass
				 






			online_ref = Entry(insurance, width=40, borderwidth=5)
			online_ref.grid(row=0,column=1, padx=20,pady=10)
			bank_name = Entry(insurance, width=40, borderwidth=5)
			bank_name.grid(row=1,column=1, padx=20,pady=10)
			on_date = Entry(insurance, width=40, borderwidth=5)
			on_date.grid(row=2,column=1, padx=20,pady=10)
			veh_no = Entry(insurance, width=40, borderwidth=5)
			veh_no.grid(row=3,column=1, padx=20,pady=10)
			ph_no = Entry(insurance, width=40, borderwidth=5)
			ph_no.grid(row=4,column=1, padx=20,pady=10)
			renewal = Entry(insurance, width=40, borderwidth=5)
			renewal.grid(row=5,column=1, padx=20,pady=10)
			name_transfer = Entry(insurance, width=40, borderwidth=5)
			name_transfer.grid(row=6,column=1, padx=20,pady=10)
			additions = Entry(insurance, width=40, borderwidth=5)
			additions.grid(row=7,column=1, padx=20,pady=10)
			button_1 = Button(insurance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=8, column=0, columnspan=2)
			mybutton_2 = Button(insurance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=9, column=0, columnspan=2)


			online_label=Label(insurance, text="ONLINE REF NUMBER")
			online_label.grid(row=0, column=0)
			bank_name_label=Label(insurance, text="BANK ACCOUNT")
			bank_name_label.grid(row=1, column=0)
			on_date_label=Label(insurance, text="ON DATE")
			on_date_label.grid(row=2, column=0)
			veh_no_label=Label(insurance, text="VEHICLE NUMBER")
			veh_no_label.grid(row=3, column=0)
			ph_no_label=Label(insurance, text="PHONE NUMBER")
			ph_no_label.grid(row=4, column=0)
			renewal_label=Label(insurance, text="RENEWAL AMOUNT")
			renewal_label.grid(row=5, column=0)
			name_transfer_label=Label(insurance, text="NAME TRANSFER")
			name_transfer_label.grid(row=6, column=0)
			additions_label=Label(insurance, text="ADDITIONS IFANY")
			additions_label.grid(row=7, column=0)

		if first == "ONLINE" and second == "NEW CAR":
			new_car = Toplevel(newwindow_3)
			new_car.title("ONLINE NEW CAR")


			def back():
				online_ref.delete(0, END)
				on_date.delete(0, END)
				bank_name.delete(0, END)
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				new_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT ON DATE " + on_date.get() + "  TOWARDS NEW CAR BOOKING AMOUNT FOR "+ description + " PH NO " + phone + " ONLINE REF NO " + online_ref.get() + " " + additions.get()) 
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT ON DATE " + on_date.get() + "  TOWARDS NEW CAR PART AMOUNT FOR " + description + " PH NO " + phone + " ONLINE REF NO " + online_ref.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT ON DATE " + on_date.get() + "  TOWARDS NEW CAR FINAL AMOUNT FOR " + description + " PH NO " + phone + " ONLINE REF NO " + online_ref.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT ON DATE " + on_date.get() + "  TOWARDS NEW CAR FINANCE AMOUNT FOR " + description + " PH NO " + phone + " ONLINE REF NO " + online_ref.get() + " " + additions.get())
							pass
						pass
					pass
				pass



			online_ref = Entry(new_car, width=40, borderwidth=5)
			online_ref.grid(row=0,column=1, padx=20,pady=10)
			bank_name = Entry(new_car, width=40, borderwidth=5)
			bank_name.grid(row=1,column=1, padx=20,pady=10)
			on_date = Entry(new_car, width=40, borderwidth=5)
			on_date.grid(row=2,column=1, padx=20,pady=10)
			ph_no = Entry(new_car, width=40, borderwidth=5)
			ph_no.grid(row=3,column=1, padx=20,pady=10)
			veh_desc = Entry(new_car, width=40, borderwidth=5)
			veh_desc.grid(row=4,column=1, padx=20,pady=10)
			booking_amount = Entry(new_car, width=40, borderwidth=5)
			booking_amount.grid(row=5,column=1, padx=20,pady=10)
			part_amount = Entry(new_car, width=40, borderwidth=5)
			part_amount.grid(row=6,column=1, padx=20,pady=10)
			final_amount = Entry(new_car, width=40, borderwidth=5)
			final_amount.grid(row=7,column=1, padx=20,pady=10)
			finance_amount = Entry(new_car, width=40, borderwidth=5)
			finance_amount.grid(row=8,column=1, padx=20,pady=10)
			additions = Entry(new_car, width=40, borderwidth=5)
			additions.grid(row=9,column=1, padx=20,pady=10)
			button_1 = Button(new_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=10, column=0, columnspan=2)
			mybutton_2 = Button(new_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=11, column=0, columnspan=2)


			online_label=Label(new_car, text="REF NO")
			online_label.grid(row=0, column=0)
			bank_name_label=Label(new_car, text="BANK NAME")
			bank_name_label.grid(row=1, column=0)
			on_date_label=Label(new_car, text="ON DATE")
			on_date_label.grid(row=2, column=0)
			ph_no_label=Label(new_car, text="PHONE NO")
			ph_no_label.grid(row=3, column=0)
			veh_desc_label=Label(new_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=4, column=0)
			booking_amount_label=Label(new_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=5, column=0)
			part_amount_label=Label(new_car, text="PART AMOUNT")
			part_amount_label.grid(row=6, column=0)
			final_amount_label=Label(new_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=7, column=0)
			finance_amount_label=Label(new_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=8, column=0)
			additions_label=Label(new_car, text="ADDITIONS IFANY")
			additions_label.grid(row=9, column=0)

		if first == "ONLINE" and second == "USED CAR":
			used_car = Toplevel(newwindow_3)
			used_car.title("ONLINE USED CAR")


			def back():
				on_date.delete(0, END)
				bank_name.delete(0, END)
				online_ref.delete(0, END)
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				used_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT " + "ON DATE " + on_date.get() + " TOWARDS USED CAR BOOKING AMOUNT FOR VEH NO " + veh_no.get() + " VEH PRICE " + veh_price.get() + " PH NO " + phone + " " + description + " REF NO " + online_ref.get() + " "  + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT " + "ON DATE " + on_date.get() + " TOWARDS USED CAR PART AMOUNT FOR VEH NO " + veh_no.get() + " VEH PRICE " + veh_price.get() + " PH NO " + phone + " " + description + " REF NO " + online_ref.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT " + "ON DATE " + on_date.get() + " TOWARDS USED CAR FINAL AMOUNT FOR VEH NO " + veh_no.get() + " VEH PRICE " + veh_price.get() + " PH NO " + phone + " " + description + " REF NO " + online_ref.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT " + "ON DATE " + on_date.get() + " TOWARDS USED CAR FINANCE AMOUNT FOR VEH NO " + veh_no.get() + " VEH PRICE " + veh_price.get() + " PH NO " + phone + " " + description + " REF NO " + online_ref.get() + " " + additions.get())
							pass
						pass
					pass
				pass



			online_ref = Entry(used_car, width=40, borderwidth=5)
			online_ref.grid(row=0,column=1, padx=20,pady=10)
			bank_name = Entry(used_car, width=40, borderwidth=5)
			bank_name.grid(row=1,column=1, padx=20,pady=10)
			on_date = Entry(used_car, width=40, borderwidth=5)
			on_date.grid(row=2,column=1, padx=20,pady=10)
			veh_no = Entry(used_car, width=40, borderwidth=5)
			veh_no.grid(row=3,column=1, padx=20,pady=10)
			ph_no = Entry(used_car, width=40, borderwidth=5)
			ph_no.grid(row=4,column=1, padx=20,pady=10)
			veh_price = Entry(used_car, width=40, borderwidth=5)
			veh_price.grid(row=5,column=1, padx=20,pady=10)
			veh_desc = Entry(used_car, width=40, borderwidth=5)
			veh_desc.grid(row=6,column=1, padx=20,pady=10)
			booking_amount = Entry(used_car, width=40, borderwidth=5)
			booking_amount.grid(row=7,column=1, padx=20,pady=10)
			part_amount = Entry(used_car, width=40, borderwidth=5)
			part_amount.grid(row=8,column=1, padx=20,pady=10)
			final_amount = Entry(used_car, width=40, borderwidth=5)
			final_amount.grid(row=9,column=1, padx=20,pady=10)
			finance_amount = Entry(used_car, width=40, borderwidth=5)
			finance_amount.grid(row=10,column=1, padx=20,pady=10)
			additions = Entry(used_car, width=40, borderwidth=5)
			additions.grid(row=11,column=1, padx=20,pady=10)
			button_1 = Button(used_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=12, column=0, columnspan=2)
			mybutton_2 = Button(used_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=13, column=0, columnspan=2)


			online_label=Label(used_car, text="ONLINE REF NO")
			online_label.grid(row=0, column=0)
			bank_name_label=Label(used_car, text="BANK NAME")
			bank_name_label.grid(row=1, column=0)
			on_date_label=Label(used_car, text="ON DATE")
			on_date_label.grid(row=2, column=0)
			veh_no_label=Label(used_car, text="VEH NO")
			veh_no_label.grid(row=3, column=0)
			ph_no_label=Label(used_car, text="PHONE NUMBER")
			ph_no_label.grid(row=4, column=0)
			veh_price_label=Label(used_car, text="VEH PRICE")
			veh_price_label.grid(row=5, column=0)
			veh_desc_label=Label(used_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=6, column=0)
			booking_amount_label=Label(used_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=7, column=0)
			part_amount_label=Label(used_car, text="PART AMOUNT")
			part_amount_label.grid(row=8, column=0)
			final_amount_label=Label(used_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=9, column=0)
			finance_amount_label=Label(used_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=10, column=0)
			additions_label=Label(used_car, text="ADDITIONS IFANY")
			additions_label.grid(row=11, column=0)

		if first == "ONLINE"  and second == "ADVANCE":
			advance = Toplevel(newwindow_3)
			advance.title("ONLINE ADVANCE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				advance_catagory.delete(0, END)
				additional_comment.delete(0, END)
				advance.destroy()


			def SUBMIT():
				text=Text(advance, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "BEING ONLINE AMOUNT CREDITED IN " + bank_name.get() + " BANK ACCOUNT " + " ON DATE " + on_date.get() + " TOWARDS " + advance_catagory.get() + " ADVANCE AMOUNT " + " FOR VEH NO " + veh_no.get() + " PHONE NUMBER " + ph_no.get() + " REFFERENCE NO " + online_ref.get() + " " + additional_comment.get())




			online_ref = Entry(advance, width=40, borderwidth=5)
			online_ref.grid(row=0,column=1, padx=20,pady=10)
			bank_name = Entry(advance, width=40, borderwidth=5)
			bank_name.grid(row=1,column=1, padx=20,pady=10)
			on_date = Entry(advance, width=40, borderwidth=5)
			on_date.grid(row=2,column=1, padx=20,pady=10)
			veh_no = Entry(advance, width=40, borderwidth=5)
			veh_no.grid(row=3,column=1, padx=20,pady=10)
			ph_no = Entry(advance, width=40, borderwidth=5)
			ph_no.grid(row=4,column=1, padx=20,pady=10)
			advance_catagory = Entry(advance, width=40, borderwidth=5)
			advance_catagory.grid(row=5,column=1, padx=20,pady=10)
			additional_comment = Entry(advance, width=40, borderwidth=5)
			additional_comment.grid(row=6,column=1, padx=20,pady=10)
			button_1 = Button(advance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=7, column=0, columnspan=2)
			mybutton_2 = Button(advance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=8, column=0, columnspan=2)


			online_label=Label(advance, text="REFFERENCE NO")
			online_label.grid(row=0, column=0)
			bank_name_label=Label(advance, text="BANK NAME")
			bank_name_label.grid(row=1, column=0)
			on_date_label=Label(advance, text="ON DATE")
			on_date_label.grid(row=2, column=0)
			veh_no_label=Label(advance, text="VEH NO")
			veh_no_label.grid(row=3, column=0)
			ph_no_label=Label(advance, text="PHONE NO")
			ph_no_label.grid(row=4, column=0)
			advance_catagory_label=Label(advance, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=5, column=0)
			additional_comment_label=Label(advance, text="ADDITIONS IFANY")
			additional_comment_label.grid(row=6, column=0)

	welcome_label=Label(newwindow_3, text="WELCOME TO NARRATION GENERATOR", fg ="green", font="poppins")
	welcome_label.grid(row=0, column=0 , columnspan=3)
	e = Entry(newwindow_3, width= 65)
	e.grid(row = 2, column=0, columnspan=3)
	mybutton_1 = Button(newwindow_3, text="SERVICE" ,padx=55, pady=20, command= lambda:on_click("SERVICE"),bg="#FF5B09", fg="black", borderwidth=4)
	mybutton_2 = Button(newwindow_3, text="MDS" ,padx=64, pady=20, command= lambda:on_click("MDS"),bg="#FFE303", fg="black", borderwidth=4)
	mybutton_3 = Button(newwindow_3, text="INSURANCE" ,padx=45, pady=20, command= lambda:on_click("INSURANCE"), bg="#AADD00", fg="black", borderwidth=4)

	mybutton_4 = Button(newwindow_3, text="NEW CAR" ,padx=50, pady=20, command= lambda:on_click("NEW CAR"), bg="#eedd82", fg="black", borderwidth=4)
	mybutton_5 = Button(newwindow_3, text="USED CAR" ,padx=50, pady=20, command= lambda:on_click("USED CAR"), bg="#82eedd", fg="black", borderwidth=4)
	mybutton_6 = Button(newwindow_3, text="ADVANCE" ,padx=50, pady=20, command= lambda:on_click("ADVANCE"), bg="#dd82ee", fg="black", borderwidth=4)

	mybutton_7 = Button(newwindow_3, text="COUNTER SALE" ,padx=36, pady=20, command= lambda:on_click("COUNTER SALE"),bg="#ffbf00", fg="black", borderwidth=4)
	mybutton_8 = Button(newwindow_3, text="ACCESSORIES" ,padx=42, pady=20, command= lambda:on_click("ACCESSORIES"), bg="#eea782", fg="black", borderwidth=4)
	mybutton_9 = Button(newwindow_3, text="BACK" ,padx=60, pady=20 , command=mainmenu , bg="#FF0000" , fg="black", borderwidth=4)


	mybutton_1.grid(row = 3, column=0)
	mybutton_2.grid(row = 3, column=1)
	mybutton_3.grid(row = 3, column=2)

	mybutton_4.grid(row = 4, column=0)
	mybutton_5.grid(row = 4, column=1)
	mybutton_6.grid(row = 4, column=2)

	mybutton_7.grid(row =5, column=0)
	mybutton_8.grid(row =5, column=1)
	mybutton_9.grid(row =5, column=2)

	welcome_label=Label(newwindow_3, text="CREATED BY", fg="green", font="poppins")
	welcome_label.grid(row=7, column=0 , columnspan=3)
	welcome_label=Label(newwindow_3, text="Y SAI SUMANTH", fg="green", font="poppins")
	welcome_label.grid(row=8, column=0 , columnspan=3)

def newwindow_4(text):
	entry.delete(0, END)
	entry.insert(0,text)
	global first
	first = entry.get()
	newwindow_4= Toplevel(root)
	newwindow_4.title("CHEQUE")
	newwindow_4.geometry("500x500")
	newwindow_4.configure(bg="#FFD39B")







	def mainmenu():
		newwindow_4.destroy()

	def on_click(text):
		e.delete(0, END)
		e.insert(0, text)
		global second
		second = e.get()

		if first == "CHEQUE" and second == "SERVICE":
			service = Toplevel(newwindow_4)
			service.title("CHEQUE SERVICE")

			def back():
				cheque_no.delete(0,END)
				veh_no.delete(0, END)
				jc_no.delete(0, END)
				br_no.delete(0, END)
				loyality_points.delete(0, END)
				liability_date.delete(0, END)
				liability_amount.delete(0, END)
				liability_company.delete(0, END)
				advance_catagory.delete(0, END)
				advance_amount.delete(0, END)
				ph_no.delete(0, END)

				service.destroy()


			def SUBMIT():
				
				global a
				global b
				global c
				global d
				global e
				global f
				global g
				global h
				global i
				global g

				a = veh_no.get()
				b = jc_no.get()
				c = br_no.get()
				d = ph_no.get()
				e = liability_company.get()
				f = liability_date.get()
				g = liability_amount.get()
				h = advance_catagory.get()
				i = advance_amount.get()
				j = loyality_points.get()
				global cashwithoutliability
				cashwithoutliability = "BEING CHEQUE RECEIVED TOWARDS VEH NO "  + a + " JC NO " + b + " BR NO " + c + " PH NO " + d + " CHEQUE NUMBER " + cheque_no.get() 
				global liability
				liability = "INSURANCE COMPANY" + " " + e + " " +"DATE"+ " " + f + " " +"INSURANCE AMOUNT"+ " " + g
			



				if (len(liability) == 42):
					if(len(j) <= 0):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + additions.get()) 
						pass
					pass
				if(len(j) > 0):
					if(len(liability) == 42):
						if(len(i) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(i) > 0):
					if(len(liability) == 42):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) > 42):
					if(len(j) <= 0):
						if(len(i) <=0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + additions.get())
						pass
					pass
				if(len(liability)>42):
					if(len(j)>0):
						if(len(i) <= 0 ):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(i) >0):
						if(len(j) <= 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				if(len(liability) >42):
					if(len(j) > 0):
						if(len(i) > 0):
							text=Text(service, width=40, height=6,padx=10,pady=10)
							text.grid(row=1, column=0, columnspan=2)
							text.insert(END, cashwithoutliability + " " + liability + " LOYALITY POINTS " + j + " " + h + " ADVANCE AMOUNT " + i + " " + additions.get())
						pass
					pass
				pass



			cheque_no = Entry(service,width=40, borderwidth=5)	
			cheque_no.grid(row= 0, column =1, padx=20, pady=10)	
			veh_no=Entry(service,width=40, borderwidth=5)
			veh_no.grid(row=1, column=1, padx=20, pady=10)
			jc_no= Entry(service,width=40, borderwidth=5)
			jc_no.grid(row=2, column=1, padx=20, pady=10)
			br_no= Entry(service,width=40, borderwidth=5)
			br_no.grid(row=3, column=1, padx=20, pady=10)
			ph_no= Entry(service,width=40, borderwidth=5)
			ph_no.grid(row=4, column=1, padx=20, pady=10)
			loyality_points= Entry(service,width=40, borderwidth=5)
			loyality_points.grid(row=5, column=1, padx=20, pady=10)
			liability_company= Entry(service,width=40, borderwidth=5)
			liability_company.grid(row=6, column=1, padx=20, pady=10)
			liability_date= Entry(service,width=40,borderwidth=5)
			liability_date.grid(row=7, column=1, padx=20, pady=10)
			liability_amount= Entry(service,width=40, borderwidth=5)
			liability_amount.grid(row=8, column=1, padx=20, pady=10)
			advance_catagory = Entry(service, width=40, borderwidth=5)
			advance_catagory.grid(row=9, column=1, padx=20, pady=10)
			advance_amount = Entry(service, width=40, borderwidth=5)
			advance_amount.grid(row=10, column=1, padx=20,pady=10)
			additions = Entry(service, width=40, borderwidth=5)
			additions.grid(row=11, column=1, padx=20,pady=10)
			button_1 = Button(service, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=12, column=0, columnspan=2)
			mybutton_2 = Button(service, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=13, column=0, columnspan=2)

			cheque_label=Label(service, text="CHEQUE NUMBER")
			cheque_label.grid(row=0, column=0)
			veh_no_label=Label(service, text="VEHICLE NUMBER")
			veh_no_label.grid(row=1, column=0)
			jc_no_label=Label(service, text="JOB CARD NUMBER")
			jc_no_label.grid(row=2, column=0)
			br_no_label=Label(service, text="BILL NUMBER")
			br_no_label.grid(row=3, column=0)
			ph_no_label=Label(service, text="PHONE NUMBER")
			ph_no_label.grid(row=4, column=0)
			loyality_no_label=Label(service, text="LOYALITY POINTS")
			loyality_no_label.grid(row=5, column=0)
			company_no_label=Label(service, text="LIABILITY COMPANY")
			company_no_label.grid(row=6, column=0)
			date_no_label=Label(service, text="LIABILITY DATE")
			date_no_label.grid(row=7, column=0)
			amount_no_label=Label(service, text="LIABILITY AMOUNT")
			amount_no_label.grid(row=8, column=0)
			advance_catagory_label = Label(service, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=9, column=0)
			advance_amount_label = Label(service, text="ADVANCE AMOUNT")
			advance_amount_label.grid(row=10, column=0)
			additions_label = Label(service, text="ADVANCE AMOUNT")
			additions_label.grid(row=11, column=0)

		if first == "CHEQUE" and second == "INSURANCE":
			insurance = Toplevel(newwindow_4)
			insurance.title("CHEQUE INSURANCE")

			def back():
				cheque_no.delete(0,END)
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				renewal.delete(0, END)
				name_transfer.delete(0, END)
				cheque_no.delete(0, END)
				insurance.destroy()

			def SUBMIT():

				ren = renewal.get()
				nt = name_transfer.get()

				if(len(ren) > 0):
					if(len(nt) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "BEING CHEQUE RECEIVED TOWARDS INSURANCE RENEWAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " CHEQUE NUMBER " + cheque_no.get() + " " + additions.get())
					pass
				if(len(nt) > 0):
					if(len(ren) <= 0):
						text=Text(insurance, width=40, height=6,padx=10,pady=10)
						text.grid(row=1, column=0, columnspan=2)
						text.insert(END, "BEING CHEQUE RECEIVED TOWARDS INSURANCE NAME TRANSFER AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " CHEQUE NUMBER " + cheque_no.get() + " " + additions.get())
					pass
				 






			cheque_no = Entry(insurance, width=40, borderwidth=5)
			cheque_no.grid(row=0,column=1, padx=20,pady=10)
			veh_no = Entry(insurance, width=40, borderwidth=5)
			veh_no.grid(row=1,column=1, padx=20,pady=10)
			ph_no = Entry(insurance, width=40, borderwidth=5)
			ph_no.grid(row=2,column=1, padx=20,pady=10)
			renewal = Entry(insurance, width=40, borderwidth=5)
			renewal.grid(row=3,column=1, padx=20,pady=10)
			name_transfer = Entry(insurance, width=40, borderwidth=5)
			name_transfer.grid(row=4,column=1, padx=20,pady=10)
			additions = Entry(insurance, width=40, borderwidth=5)
			additions.grid(row=5,column=1, padx=20,pady=10)
			button_1 = Button(insurance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=6, column=0, columnspan=2)
			mybutton_2 = Button(insurance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=7, column=0, columnspan=2)


			cheque_label=Label(insurance, text="CHEQUE NUMBER")
			cheque_label.grid(row=0, column=0)
			veh_no_label=Label(insurance, text="VEHICLE NUMBER")
			veh_no_label.grid(row=1, column=0)
			ph_no_label=Label(insurance, text="PHONE NUMBER")
			ph_no_label.grid(row=2, column=0)
			renewal_label=Label(insurance, text="RENEWAL AMOUNT")
			renewal_label.grid(row=3, column=0)
			name_transfer_label=Label(insurance, text="NAME TRANSFER")
			name_transfer_label.grid(row=4, column=0)
			additions_label=Label(insurance, text="ADDITIONS IFANY")
			additions_label.grid(row=5, column=0)

		if first == "CHEQUE" and second == "NEW CAR":
			new_car = Toplevel(newwindow_4)
			new_car.title("CHEQUE NEW CAR")


			def back():
				cheque_no.delete(0,END)
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				new_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CHEQUE  RECEIVED TOWARDS NEW CAR BOOKING AMOUNT FOR " + description + " PH NO " + phone + " CHEQUE NO " + cheque_no.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CHEQUE  RECEIVED TOWARDS NEW CAR PART AMOUNT FOR " + description + " PH NO " + phone + " CHEQUE NO " + cheque_no.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CHEQUE  RECEIVED TOWARDS NEW CAR FINAL AMOUNT FOR " + description + " PH NO " + phone + " CHEQUE NO " + cheque_no.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(new_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CHEQUE  RECEIVED TOWARDS NEW CAR FINANCE AMOUNT FOR " + description + " PH NO " + phone + " CHEQUE NO " + cheque_no.get() + " " + additions.get())
							pass
						pass
					pass
				pass



			cheque_no = Entry(new_car, width=40, borderwidth=5)
			cheque_no.grid(row=0,column=1, padx=20,pady=10)
			ph_no = Entry(new_car, width=40, borderwidth=5)
			ph_no.grid(row=1,column=1, padx=20,pady=10)
			veh_desc = Entry(new_car, width=40, borderwidth=5)
			veh_desc.grid(row=2,column=1, padx=20,pady=10)
			booking_amount = Entry(new_car, width=40, borderwidth=5)
			booking_amount.grid(row=3,column=1, padx=20,pady=10)
			part_amount = Entry(new_car, width=40, borderwidth=5)
			part_amount.grid(row=4,column=1, padx=20,pady=10)
			final_amount = Entry(new_car, width=40, borderwidth=5)
			final_amount.grid(row=5,column=1, padx=20,pady=10)
			finance_amount = Entry(new_car, width=40, borderwidth=5)
			finance_amount.grid(row=6,column=1, padx=20,pady=10)
			additions = Entry(new_car, width=40, borderwidth=5)
			additions.grid(row=7,column=1, padx=20,pady=10)
			button_1 = Button(new_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=8, column=0, columnspan=2)
			mybutton_2 = Button(new_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=9, column=0, columnspan=2)


			cheque_label=Label(new_car, text="CHEQUE NO")
			cheque_label.grid(row=0, column=0)
			ph_no_label=Label(new_car, text="PHONE NUMBER")
			ph_no_label.grid(row=1, column=0)
			veh_desc_label=Label(new_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=2, column=0)
			booking_amount_label=Label(new_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=3, column=0)
			part_amount_label=Label(new_car, text="PART AMOUNT")
			part_amount_label.grid(row=4, column=0)
			final_amount_label=Label(new_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=5, column=0)
			finance_amount_label=Label(new_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=6, column=0)
			additions_label=Label(new_car, text="ADDITIONS IFANY")
			additions_label.grid(row=7, column=0)

		if first == "CHEQUE" and second == "USED CAR":
			used_car = Toplevel(newwindow_4)
			used_car.title("CHEQUE USED CAR")


			def back():
				cheque_no.delete(0, END)
				ph_no.delete(0,END)
				veh_desc.delete(0,END)
				booking_amount.delete(0,END)
				part_amount.delete(0,END)
				final_amount.delete(0,END)
				finance_amount.delete(0,END)
				used_car.destroy()


			def SUBMIT():
				phone =ph_no.get()
				description =veh_desc.get()
				booking = booking_amount.get()
				part = part_amount.get()
				final = final_amount.get()
				finance =finance_amount.get()

				if(len(booking) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CHEQUE RECEIVED TOWARDS USED CAR BOOKING AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " CHEQUE NO " + cheque_no.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(part) > 0):
					if(len(booking) <=0):
						if(len(final) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CHEQUE RECEIVED TOWARDS USED CAR PART AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " CHEQUE NO " + cheque_no.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(final) > 0):
					if(len(part) <=0):
						if(len(booking) <=0):
							if(len(finance) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CHEQUE RECEIVED TOWARDS USED CAR FINAL AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " CHEQUE NO " + cheque_no.get() + " " + additions.get())
							pass
						pass
					pass
				if(len(finance) > 0):
					if(len(part) <=0):
						if(len(final) <=0):
							if(len(booking) <=0):
								text=Text(used_car, width=40, height=6,padx=10,pady=10)
								text.grid(row=1, column=0, columnspan=2)
								text.insert(END, "BEING CHEQUE RECEIVED TOWARDS USED CAR FINANCE AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + phone + " VEH PRICE " + veh_price.get() + " " + description + " CHEQUE NO " + cheque_no.get() + " " + additions.get())
							pass
						pass
					pass
				pass



			cheque_no = Entry(used_car, width=40, borderwidth=5)
			cheque_no.grid(row=0,column=1, padx=20,pady=10)
			veh_no = Entry(used_car, width=40, borderwidth=5)
			veh_no.grid(row=1,column=1, padx=20,pady=10)
			ph_no = Entry(used_car, width=40, borderwidth=5)
			ph_no.grid(row=2,column=1, padx=20,pady=10)
			veh_price = Entry(used_car, width=40, borderwidth=5)
			veh_price.grid(row=3,column=1, padx=20,pady=10)
			veh_desc = Entry(used_car, width=40, borderwidth=5)
			veh_desc.grid(row=4,column=1, padx=20,pady=10)
			booking_amount = Entry(used_car, width=40, borderwidth=5)
			booking_amount.grid(row=5,column=1, padx=20,pady=10)
			part_amount = Entry(used_car, width=40, borderwidth=5)
			part_amount.grid(row=6,column=1, padx=20,pady=10)
			final_amount = Entry(used_car, width=40, borderwidth=5)
			final_amount.grid(row=7,column=1, padx=20,pady=10)
			finance_amount = Entry(used_car, width=40, borderwidth=5)
			finance_amount.grid(row=8,column=1, padx=20,pady=10)
			additions = Entry(used_car, width=40, borderwidth=5)
			additions.grid(row=9,column=1, padx=20,pady=10)
			button_1 = Button(used_car, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=10, column=0, columnspan=2)
			mybutton_2 = Button(used_car, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=11, column=0, columnspan=2)


			cheque_label=Label(used_car, text="CHEQUE NO")
			cheque_label.grid(row=0, column=0)
			veh_no_label=Label(used_car, text="VEH NO")
			veh_no_label.grid(row=1, column=0)
			ph_no_label=Label(used_car, text="PHONE NUMBER")
			ph_no_label.grid(row=2, column=0)
			veh_price_label=Label(used_car, text="VEH PRICE")
			veh_price_label.grid(row=3, column=0)
			veh_desc_label=Label(used_car, text="VEHICLE DESCRIPTION")
			veh_desc_label.grid(row=4, column=0)
			booking_amount_label=Label(used_car, text="BOOKING AMOUNT")
			booking_amount_label.grid(row=5, column=0)
			part_amount_label=Label(used_car, text="PART AMOUNT")
			part_amount_label.grid(row=6, column=0)
			final_amount_label=Label(used_car, text="FINAL AMOUNT")
			final_amount_label.grid(row=7, column=0)
			finance_amount_label=Label(used_car, text="FINANCE AMOUNT")
			finance_amount_label.grid(row=8, column=0)
			additions_label=Label(used_car, text="ADDITIONS IFANY")
			additions_label.grid(row=9, column=0)

		if first == "CHEQUE"  and second == "ADVANCE":
			advance = Toplevel(newwindow_4)
			advance.title("CHEQUE ADVANCE")

			def back():
				veh_no.delete(0, END)
				ph_no.delete(0, END)
				advance_catagory.delete(0, END)
				additional_comment.delete(0, END)
				advance.destroy()


			def SUBMIT():
				text=Text(advance, width=40, height=6,padx=10,pady=10)
				text.grid(row=1, column=0, columnspan=2)
				text.insert(END, "BEING CHEQUE RECEIVED TOWARDS " + advance_catagory.get() + " ADVANCE AMOUNT FOR VEH NO " + veh_no.get() + " PH NO " + ph_no.get() + " " +additional_comment.get() + " CHEQUE NO " + cheque_no.get())



			cheque_no = Entry(advance, width=40, borderwidth=5)
			cheque_no.grid(row=0,column=1, padx=20,pady=10)
			veh_no = Entry(advance, width=40, borderwidth=5)
			veh_no.grid(row=1,column=1, padx=20,pady=10)
			ph_no = Entry(advance, width=40, borderwidth=5)
			ph_no.grid(row=2,column=1, padx=20,pady=10)
			advance_catagory = Entry(advance, width=40, borderwidth=5)
			advance_catagory.grid(row=3,column=1, padx=20,pady=10)
			additional_comment = Entry(advance, width=40, borderwidth=5)
			additional_comment.grid(row=4,column=1, padx=20,pady=10)
			button_1 = Button(advance, text="SUBMIT", padx=40, pady=20, command=SUBMIT, bg="#00FF00", fg="black", borderwidth=4)
			button_1.grid(row=5, column=0, columnspan=2)
			mybutton_2 = Button(advance, text="BACK" ,padx=40,pady=20, command=back, bg="#FF0000", fg="black", borderwidth=4)
			mybutton_2.grid(row=6, column=0, columnspan=2)


			cheque_label=Label(advance, text="CHEQUE NO")
			cheque_label.grid(row=0, column=0)
			veh_no_label=Label(advance, text="VEH NO")
			veh_no_label.grid(row=1, column=0)
			ph_no_label=Label(advance, text="PHONE NO")
			ph_no_label.grid(row=2, column=0)
			advance_catagory_label=Label(advance, text="ADVANCE CATEGORY")
			advance_catagory_label.grid(row=3, column=0)
			additional_comment_label=Label(advance, text="ADDITIONS IFANY")
			additional_comment_label.grid(row=4, column=0)

	welcome_label=Label(newwindow_4, text="WELCOME TO NARRATION GENERATOR", fg ="green", font="poppins")
	welcome_label.grid(row=0, column=0 , columnspan=3)
	e = Entry(newwindow_4, width= 65)
	e.grid(row = 2, column=0, columnspan=3)
	mybutton_1 = Button(newwindow_4, text="SERVICE" ,padx=55, pady=20, command= lambda:on_click("SERVICE"),bg="#FF5B09", fg="black", borderwidth=4)
	mybutton_2 = Button(newwindow_4, text="MDS" ,padx=64, pady=20, command= lambda:on_click("MDS"),bg="#FFE303", fg="black", borderwidth=4)
	mybutton_3 = Button(newwindow_4, text="INSURANCE" ,padx=45, pady=20, command= lambda:on_click("INSURANCE"), bg="#AADD00", fg="black", borderwidth=4)

	mybutton_4 = Button(newwindow_4, text="NEW CAR" ,padx=50, pady=20, command= lambda:on_click("NEW CAR"), bg="#eedd82", fg="black", borderwidth=4)
	mybutton_5 = Button(newwindow_4, text="USED CAR" ,padx=50, pady=20, command= lambda:on_click("USED CAR"), bg="#82eedd", fg="black", borderwidth=4)
	mybutton_6 = Button(newwindow_4, text="ADVANCE" ,padx=50, pady=20, command= lambda:on_click("ADVANCE"), bg="#dd82ee", fg="black", borderwidth=4)

	mybutton_7 = Button(newwindow_4, text="COUNTER SALE" ,padx=36, pady=20, command= lambda:on_click("COUNTER SALE"),bg="#ffbf00", fg="black", borderwidth=4)
	mybutton_8 = Button(newwindow_4, text="ACCESSORIES" ,padx=42, pady=20, command= lambda:on_click("ACCESSORIES"), bg="#eea782", fg="black", borderwidth=4)
	mybutton_9 = Button(newwindow_4, text="BACK" ,padx=60, pady=20 , command=mainmenu , bg="#FF0000" , fg="black", borderwidth=4)


	mybutton_1.grid(row = 3, column=0)
	mybutton_2.grid(row = 3, column=1)
	mybutton_3.grid(row = 3, column=2)

	mybutton_4.grid(row = 4, column=0)
	mybutton_5.grid(row = 4, column=1)
	mybutton_6.grid(row = 4, column=2)

	mybutton_7.grid(row =5, column=0)
	mybutton_8.grid(row =5, column=1)
	mybutton_9.grid(row =5, column=2)

	welcome_label=Label(newwindow_4, text="CREATED BY", fg="green", font="poppins")
	welcome_label.grid(row=7, column=0 , columnspan=3)
	welcome_label=Label(newwindow_4, text="Y SAI SUMANTH", fg="green", font="poppins")
	welcome_label.grid(row=8, column=0 , columnspan=3)






#e =Entry(root, width=40, borderwidth=5)
#e.grid(row=0, column=0, columnspan=3, padx=10 ,pady=10)
#e.insert(0, "Enter Your Favorite: ")
welcome_label=Label(root, text="WELCOME TO NARRATION GENERATOR", fg ="green", font="poppins")
welcome_label.grid(row=0, column=0 , columnspan=3)
entry=Entry(root, width= 65)
entry.grid(row = 2, column=0, columnspan=3)


button_1 =Button(root, text="CASH" , padx=58, pady=20, command=lambda:newwindow("CASH") , bg="yellow", fg="black",borderwidth=4)
#button_1.pack()
button_2 =Button(root, text="CARD" , padx=58, pady=20, command=lambda:newwindow_1("CARD"),bg ="#FF8C00" , fg="black",borderwidth=4)
#button_2.pack()
button_3 =Button(root, text="BHIM" , padx=66, pady=20, command=lambda:newwindow_2("BHIM"),bg="#BCEE68" ,fg="black",borderwidth=4)
#button_3.pack()

button_4 =Button(root, text="ONLINE" , padx=52, pady=20, command=lambda:newwindow_3("ONLINE"),bg="#1E90FF" , fg="black",borderwidth=4)
#button_4.pack()
button_5 =Button(root, text="CHEQUE" , padx=52, pady=20, command=lambda:newwindow_4("CHEQUE"), bg ="#FFD39B" ,fg="black",borderwidth=4)
#button_5.pack()
button_6 =Button(root, text="EXIT", padx=70, pady=20, command=EXIT,bg= "#FF3030" ,fg="black",borderwidth=4)
#button_6.pack()

button_1.grid(row=3, column=0 )
button_2.grid(row=3, column=1 )
button_3.grid(row=3, column=2)

button_4.grid(row=4 , column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

welcome_label=Label(root, text="CREATED BY", fg="green", font="poppins")
welcome_label.grid(row=7, column=0 , columnspan=3)
welcome_label=Label(root, text="Y SAI SUMANTH", fg="green", font="poppins")
welcome_label.grid(row=8, column=0 , columnspan=3)



root.mainloop()
