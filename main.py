from pyscript import document, display, HTML


def create_order(e):
    document.getElementById("receipt-output").innerHTML = ""  # clears previous receipt

    # get customer info
    name = document.getElementById("name").value
    contact = document.getElementById("contact").value

    # get shoulder bag checkboxes
    item1 = document.getElementById("item1")  # LV Neverfull
    item2 = document.getElementById("item2")  # Chanel Classic Flap
    item3 = document.getElementById("item3")  # Prada Re-Edition
    item4 = document.getElementById("item4")  # YSL Loulou

    # get shoulder bag quantity
    quantity1 = int(document.getElementById("quantity1").value)

    # get accessory checkboxes
    item5 = document.getElementById("item5")  # LV Wallet
    item6 = document.getElementById("item6")  # Chanel Card Holder
    item7 = document.getElementById("item7")  # Prada Keychain
    item8 = document.getElementById("item8")  # YSL Pouch

    # get add-ons (material and gift wrap)
    material = document.querySelector('input[name="material"]:checked')
    giftwrap = document.querySelector('input[name="giftwrap"]:checked')

    # get accessory quantity
    quantity2 = int(document.getElementById("quantity2").value)

        # check if any accessory item is checked
    any_accessory_checked = item5.checked or item6.checked or item7.checked or item8.checked

    # stop and show a message if an accessory is selected but material/giftwrap wasn't
    if any_accessory_checked and (material is None or giftwrap is None):
        display("Please select a material and gift wrap option for your accessory.", target="receipt-output", append=False)
        return

    bags_subtotal = 0  # starting value for shoulder bags total

    # add price to bags_subtotal only if the checkbox is checked
    if item1.checked:
        bags_subtotal += float(item1.value)

    if item2.checked:
        bags_subtotal += float(item2.value)

    if item3.checked:
        bags_subtotal += float(item3.value)

    if item4.checked:
        bags_subtotal += float(item4.value)

    # multiply shoulder bags total by quantity
    bags_subtotal = bags_subtotal * quantity1

    accessories_subtotal = 0  # starting value for accessories total

    # add price to accessories_subtotal only if the checkbox is checked
    if item5.checked:
        accessories_subtotal += float(item5.value)

    if item6.checked:
        accessories_subtotal += float(item6.value)

    if item7.checked:
        accessories_subtotal += float(item7.value)

    if item8.checked:
        accessories_subtotal += float(item8.value)

    # add material and gift wrap add-on prices only if an accessory was ordered
    if any_accessory_checked:
        accessories_subtotal += float(material.value)
        accessories_subtotal += float(giftwrap.value)

    # multiply accessories total by quantity
    accessories_subtotal = accessories_subtotal * quantity2

    # combine both subtotals
    subtotal = bags_subtotal + accessories_subtotal

    # show a message if nothing was selected at all
    if subtotal == 0:
        display("Please select at least one item before placing your order.", target="receipt-output", append=False)
        return

    # compute VAT as 12% of the subtotal
    vat = subtotal * 0.12

    # compute total amount (subtotal + VAT)
    total = subtotal + vat

    # receipt output with HTML formatting, .2f ensures 2 decimal places for currency
    receipt_output = f"""
    <p><strong>==== Receipt ====</strong></p>
    <p>Name: {name}</p>
    <p>Contact: {contact}</p>
    <p>Bags Subtotal: P{bags_subtotal:.2f}</p>
    <p>Accessories Subtotal: P{accessories_subtotal:.2f}</p>
    <p>Subtotal: P{subtotal:.2f}</p>
    <p>VAT: P{vat:.2f}</p>
    <p>Total: P{total:.2f}</p>
    """

    # wrap with HTML() so tags render instead of showing as just text
    display(HTML(receipt_output), target="receipt-output", append=False)


#SKU GENERATOR-----------

def generate_sku(event):
    document.getElementById("sku-output").innerHTML = ""
 
  
    category = document.getElementById("category").value
    product = document.getElementById("product").value
    quantity = document.getElementById("quantity").value
 
   
    if category == "" or category == "select" or product == "" or quantity == "":
        display("Please fill out all fields.", target="sku-output", append=False)
        return
 
    sku = f"{category}-{quantity}-{product}"
 
    sku_output = f"""
    <p><strong>==== SKU Generator ====</strong></p>
    <p>Category: {category}</p>
    <p>Product: {product}</p>
    <p>Quantity: {quantity}</p>
    <p><strong>Generated SKU: {sku}</strong></p>
    """
 
    display(HTML(sku_output), target="sku-output", append=False)
 
 