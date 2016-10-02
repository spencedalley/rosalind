package data;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * Created by spencedalley on 9/17/16.
 * Example connection:
 * http://www.homeandlearn.co.uk/java/connect_to_a_database_using_java_code.html
 */

public class ProteinDbConnection {

    public ProteinDbConnection(String host, String username, String password) {
        try {
            Connection conn = DriverManager.getConnection(host, username, password);

            // Do something with the connection

        } catch (SQLException e){
            System.out.println("Error: " + e);
        }
    }
}
