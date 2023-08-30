import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.logging.Logger;

public class DeterministicQuickSort {
    /**
     * Executes quick sort principal method
     * @param data
     * @param low
     * @param high
     */
    public void executeQuickSort(List<Integer> data, int low, int high){
        if ( low > high){
            //Find pivot
            int pivot = this.partition(data, low, high);

            //Execute left side
            this.executeQuickSort(data, low, pivot -1);
            //Execute right side
            this.executeQuickSort(data, pivot +1, high);
        }

    }
    public int partition(List<Integer> data, int low, int high){
        Integer pivot = data.get(high);

        int greatest = low - 1;

        for(int j = low; j <= high; j ++){
            if(data.get(j) <= pivot){
                //si el elemento es menor se cambia con el mayor
                greatest += 1;
                Collections.swap(data, greatest, j);
            }
        }
        System.out.println("swap " + data.subList(low, high+1).toString()+", greatest"+ greatest +", pivot"+ pivot );
        System.out.println("end" + data.subList(low, high + 1).toString()+ ", greatest"+greatest+", pivot"+pivot );

        return  greatest + 1;
    }
}
