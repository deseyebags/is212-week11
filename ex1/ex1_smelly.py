class OrderProcessor:
    def process_order(self, order):
        # Step 1: Validate order details
        fields = ["customer_id","items"]
        for i in fields:
            if not order.get(i):
                self.return_errors(i)
         
        # Step 2: Calculate total price
        total_price = self.compute_total(order)

        # Step 3: Apply discounts if applicable
        total_price=self.apply_discount(total_price,order)

        # Step 4: Update inventory
        self.itemised(order)

        # Step 5: Generate receipt
        receipt = self.gen_receipt(total_price,order)

        # Step 6: Send confirmation email
        self.email_send(order,receipt)
        
        return receipt
    
    def return_errors(self,field):
        errors = {
            "customer_id":"Customer ID is required.",
            "items":"Order must contain items.",
        }
        raise ValueError(errors[field])

    def compute_total(self,order):
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]
        return total_price
    
    def apply_discount(self,total,order):
        disc_code ={
                    "SUMMER20":0.8,
                    "WELCOME10":0.9,
                    }
        if order.get("discount_code") in disc_code.keys():
            total *= disc_code[order.get("discount_code")] 
        return total
    
    def itemised(self,order):
        for item in order["items"]:
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item["id"]}, reducing stock by {item["quantity"]}.")
        
    def gen_receipt(self,total_price,order):
        receipt = f"Customer ID: {order['customer_id']}\nItems:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt
    
    def email_send(self,order,receipt):
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")