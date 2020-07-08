## The Farmers Market

Farmers market is a checkout system in which certain products are sold and occasionally may have offers.
For Details check below the link (https://gist.github.com/jbartels/d75a9f5282abebe071694723a5f25f0e)

Ideal desgin would be to have different services like below.

1.Menu service
1.Basket Service
1.Offer Service
1.Products Service

More Modern design would be to divide these services into Function as service(FAAS)

But for now its coded as monolith.


#### Table of contents

1. [Enviornment Setup](#envsetup)
1. [Build](#build)
1. [Install](#install)
1. [Testing](#testing)
1. [Usage Examples](#usage)


### <a name="envsetup"></a> Environment Setup

Ensure docker is installed and is up and running.

```bash
sudo service docker status
```
Install Python3 & virtual env for development.


### <a name="build"></a> Build

1. Configure products available in store in config/products.json (TODO elobrate on schema)
2. Update offers on products in store in offers/offers.json (TODO elobrate on schema)
3. Build image

```bash
docker build -t farmers_market:1.0 .
```
### <a name="install"></a> Install

use docker run to start the checkout system

```bash
docker run -ti farmers_market:1.0 
```

#### Todo
1. make products and offers configable through volumes. In kubernetes these can be configmaps.
2. make basket a service

### <a name="testing"></a> Testing

1. python unittest is used.
2. tests are run as part of docker build.
3. to run outside docker use below command.

```bash
python -m unittest -v
```

### <a name="usage"></a> Usage Examples

Below is menu of farmers market checkout system.

            Farmers Market Checkout System)
                      A: Add item
                      V: View Basket
                      C: Checkout
                      Q: Quit/Log Out

                      Please enter your choice: 

1. pressing a/A allows user to add an item available in store.
2. pressing v/V shows current basket, offers appled, total biill
3. pressing c/C shows bill and total bill is to be paid. Basket is cleared for next customer.
4. q/Q quites the system.

#### Adding item

               Farmers Market Checkout System)
                      A: Add item
                      V: View Basket
                      C: Checkout
                      Q: Quit/Log Out

                      Please enter your choice: a
 
                    Enter Product Id:['AP1', 'CH1', 'OM1', 'MK1', 'CF1']

#### View basket
               Farmers Market Checkout System)
                      A: Add item
                      V: View Basket
                      C: Checkout
                      Q: Quit/Log Out

                      Please enter your choice: v


```
Item		Price
----		-----

AP1		 6.0
	APPL	-3.0
OM1		 3.69
--------------------------------
		 6.69
```
