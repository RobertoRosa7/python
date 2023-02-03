# No Time to Lose: Time Seires Analysis

* Handling of date data
* Time series modeling
* Moving averages
* Seasonality
* Autoregression

The Data to analyse these phenomena can be collected at regular intervals over time.  

$a \ne 0$

> The  log return is given by: $$ ({FV \over PV})$$ where FV is the **Future Value** and PV is the **Past Value**  

As expected, we have two entries for each date. We can also look at statistics such as the mean and the sum of entries.
In this case, we are going to use `resample` method for a series.  
In effect this enables us to change the time frequency in our dataset. Let us use the `M` *offset alias* to tell Pandas to create
monthly statistics.
  
| Alias | Description |
| ----- | ----------- |
| B | business day frequency |
| C | custom bunisness day frequency |
| D | calendar day frequency |
| W | weekly frequency |
| M | month-end frequency |
| Q | quarter-end frequency |
| H | hourly frequency |
| S | secondly frequency |
| N | nanoseconds
| BQ | business quarter-end frequency |
| QS | quarter start frequency |
| SM | semi-month-end frequency (15th and end of month) |
| BM | business month-end frequency |
| MS | month-start frequency |
| BH | business hour frequency |
| BQS | business quarter start frequency |
| SMS | semi-month-start frequency (1st and 15th) |
| CBM | custom business month-end frequency |
| BMS | business month start frequency |
| CBMS | custom business month-start frequency |
| A, Y | year-end frequency |
| L, ms | milliseconds |
| U, us | microseconds |
| BA, By | business year-end frequency |
| AS, YS | year-start frequency |
| T, min | minutely frequency |
| BAS, BYS | businness year-start frequency |


$$
f(x;\mu,\sigma^2) = \frac{1}{\sigma\sqrt{2\pi}}
e^{ -\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2 }
$$