library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_UNSIGNED.all;
library work;
use ieee.numeric_std.all;

entity adderpc is
    port (
        pc_old : in std_logic_vector(15 downto 0);
        pc_new : out std_logic_vector(15 downto 0)
    );
end adderpc;

architecture working of adderpc is

    constant one : std_logic_vector(15 downto 0) := "0000000000000001";
    begin
        pc_update_process:process(pc_old)
        begin
            pc_new <= pc_old + one;
        end process pc_update_process;
end working;
