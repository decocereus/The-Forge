public class NumberDisplay
{
    private int limit;
    private int value;
    public int meridianForHours;
    public int meridianForMinutes;
    /**
     * Constructor for objects of class NumberDisplay.
     * Set the limit at which the display rolls over.
     */
    public NumberDisplay(int rollOverLimit)
    {
        limit = rollOverLimit;
        value = 0;
    }
    /**
     * Return the current value.
     */
    public int getValue()
    {
        if ( value >= 13 )
        {
            return (value - 12);
        }
        else {
            value = value;
            return value;
        }
    }

    /**
     * Return the display value (that is, the current value as a two-digit
     * String. If the value is less than ten, it will be padded with a leading
     * zero).
     */
    public String getDisplayValueMinutes()
    {
        meridianForMinutes = value;
        if(value < 10) {
            return "0" + value;
        }
        else {
            return "" + value;
        }
   }
    public String getDisplayValueHours()
    {
        meridianForHours = value;
        if ( value >= 13)
        {
            value = value - 12;
            return "" + value;
        }
        else {
            return "" + value;
        }
    }
    /**
     * Set the value of the display to the new specified value. If the new
     * value is less than zero or over the limit, do nothing.
     */
    public void setValue(int replacementValue)
    {
        if((replacementValue >= 0) && (replacementValue < limit)) {
            value = replacementValue;
        }
    }

    /**
     * Increment the display value by one, rolling over to zero if the
     * limit is reached.
     */
    public void increment()
    {
        value = (value + 1) % limit;
    }
}
