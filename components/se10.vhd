library ieee;
library work;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity sign_10_extender is 
    port(
        se_ip_10 : in std_logic_vector(5 downto 0);
        se_op_10 : out std_logic_vector(15 downto 0)
        );
end sign_10_extender;

architecture working of sign_10_extender is
    begin
        sign_10_extender_process: process(se_ip_10)
        variable temp : integer;
        begin
            temp := to_integer(unsigned(se_ip_10));
            se_op_10 <= std_logic_vector(to_unsigned(temp,16));
        end process;
end working;